import { useSelector, useDispatch } from 'react-redux'
import { increment, decrement, incrementByValue } from './counterSlice'
export default function Counter() {
  const count = useSelector((state) => state.counter.count)
  const dispatch = useDispatch()
  return (
    <div>
      <button onClick={() => dispatch(increment())}>increment</button>
      <span>{count}</span>

      <button onClick={() => dispatch(decrement())}>decrement</button>
      <button onClick={() => dispatch(incrementByValue(6))}>
        incrementByValue
      </button>
    </div>
  )
}
