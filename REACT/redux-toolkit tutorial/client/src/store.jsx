// first we have configured store for state using configureStore, it simplify the process of creating a redux store inside redux application
import { configureStore } from '@reduxjs/toolkit'
import counterReducer from './counterSlice.jsx'

// creating store using configureStore and passing
export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
})
