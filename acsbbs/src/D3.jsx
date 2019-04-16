import React, { Component } from 'react';
import { connect } from 'react-redux';

function mapStateToProps(state) {
    return {
      username: state.user.username,
    }
}

class D3 extends Component {
    render() {
        return (
            <div>
                <p>{this.props.username}</p>
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    null
)(D3)