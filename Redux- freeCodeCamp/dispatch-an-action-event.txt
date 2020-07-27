const store = Redux.createStore(
  (state = {login: false}) => state
);

const loginAction = () => {
  return {
    type: 'LOGIN'
  }
};
9
// Dispatch the action here:
store.dispatch(loginAction())