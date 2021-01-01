import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import App from './App';
import {TweetsComponent} from './tweets'
import reportWebVitals from './reportWebVitals';

const appE1 = document.getElementById('root');
if (appE1) {
    ReactDOM.render(<App />, appE1);
}
const tweetsE1 = document.getElementById('tweetme-2')
if (tweetsE1){
    ReactDOM.render(<TweetsComponent />, tweetsE1);
}


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
