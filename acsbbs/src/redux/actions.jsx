export function changeUsername(username) {
  return {
    type: 'CHANGE_USERNAME',
    payload: {
        username
    }
  }
};
