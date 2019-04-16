import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import D1 from './D1';

import { Provider } from 'react-redux';
import store from './redux/store';
import { changeUsername } from './redux/actions';
import { connect } from 'react-redux';


class P1 extends Component {
    constructor(props) {
      super(props);
      this.state = {
        'username': 'abc'
      };
    }
  
    render() {
      return (
        <Provider store={store}>
          <p>{this.state.username}</p>
          <D1 />
          <button onClick={() => this.props.changeUsername('bcd')}>aaa</button>
        </Provider>
      );
    }
  }
  
  export default connect(
    null,
    { changeUsername }
  )(P1)
