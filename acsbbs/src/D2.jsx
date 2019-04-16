import React, { Component } from 'react';
import { connect } from 'react-redux';
import D3 from './D3';

function mapStateToProps(state) {
    return {
      username: state.user.username,
    }
}

class D2 extends Component {
    render() {
        return (
            <div>
                <p>{this.props.username}</p>
                <D3 />
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    null
)(D2)