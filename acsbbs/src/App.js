import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import P1 from './P1';

import { Provider } from 'react-redux';
import store from './redux/store';
import { changeUsername } from './redux/actions';
import { connect } from 'react-redux';


class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <P1 />
      </Provider>
    );
  }
}

export default App;
