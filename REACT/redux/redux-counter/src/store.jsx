import { createStore } from 'redux'

const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case 'Increment':
      return state + 1

    case 'Decrement':
      if (state > 0) {
        return state - 1
      }
      return state
    default:
      return state
  }
}

export const store = createStore(counterReducer)
