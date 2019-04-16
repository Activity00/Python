const initialState = {
  username: 'abc'
};

export default function(state = initialState, action) {
  switch (action.type) {
    case 'CHANGE_USERNAME': {
        return {
            ...state,
            'username': action.payload.username
        }
    }
    default: {
      return state;
    }
  }
}
