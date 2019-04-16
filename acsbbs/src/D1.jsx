import React, { Component } from 'react';
import { connect } from 'react-redux';
import D2 from './D2';

function mapStateToProps(state) {
    return {
      username: state.user.username,
    }
}

class D1 extends Component {
    render() {
        return (
            <div>
                <p>{this.props.username}</p>
                <D2 />
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    null
)(D1)
