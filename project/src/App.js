import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      fetched: false
    }
  }

  componentDidMount() {
    fetch('/hello')
    .then(response => response.json())
    .then(data => {
      this.setState({
        fetched: true
      })
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1> Fetched: {this.state.fetched? "Fetched": "Stil fetching..."} </h1>
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }

}

export default App;
