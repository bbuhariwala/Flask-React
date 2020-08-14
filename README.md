# Flask-React

This repository ONLY contains a Flask-React boilerplate code containerised in a docker container to resovle dependencies. You could use this to create an entire application using React as the front end and Flask server as the backend. You could use this to create any full stack application of your choice.

[Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) is an implementation of the messaging queue in python which is used to run functions asynchronously.

[Celery Beat](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html) is used to run tasks at a fixed interval of time. 

[MongoDB](https://www.mongodb.com/) MongoDB is a general purpose, document-based, distributed database built for modern application developers.

[React](https://reactjs.org/) A JavaScript library for building user interfaces

#Steps to Run

1. Create a folder 
```
mkdir flaskreact
cd flaskreact
```

2. Download or clone this repository

3. Add your dependencies in the requirements.txt file in the server folder and package.json file (For node libraries)

4. Run the following commands from the root path of the folder we created above:

```
docker-compose build
docker-compose up
```

5. Go to http://localhost:3000 in your browser
