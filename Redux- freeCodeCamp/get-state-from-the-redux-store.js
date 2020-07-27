// here reducer isn't used and an anonymous function is passed instead
const store = Redux.createStore(
  (state = 5) => state
);

// change code below this line
let currentState = store.getState()
