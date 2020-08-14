from flask import Flask, jsonify
import time
from celery import Celery
from celery.schedules import crontab
from pymongo import MongoClient
from flask_jwt_extended import set_access_cookies

app = Flask (__name__)

def make_celery(app):
    celery = Celery( app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'] )
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery

app.config['CELERY_BROKER_URL'] = 'amqp://guest@rabbitmq:5672'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

schedule = {}
schedule['pt'] = {}
schedule['pt']['task'] = 'periodic_task'
schedule['pt']['schedule'] = crontab(minute='*')
app.config['CELERYBEAT_SCHEDULE'] = schedule;

celery = make_celery(app)

HOST = 'mongodb'
PORT_NUM = 27017
DB_NAME= 'test-db-1'
COLLECTION_NAME= 'test-coll-1'

@app.route('/hello')
def hello():
    time.sleep(5)
    justATask.delay()
    result =  jsonify({"message": "Hello World Response"})
    set_access_cookies(result,"cookiefromserver")
    return result

@celery.task()
def justATask():
    connectToDB()
    print("THis is just a celery Task.")

@celery.task(name='periodic_task')
def poller():
    print("This is Task That is happening every minute")

def connectToDB():
    print("Connecting to DB")
    try:
        client = MongoClient(host=HOST,port=PORT_NUM, connect = False)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        args = {}
        args['name'] = 'Dummy'
        collection.insert_one(args)
        documents = collection.find({})
        for document in documents:
          print(document)
    except Exception as e:
        print("Mongo Exception" + str(e))
