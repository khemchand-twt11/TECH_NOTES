import { useSelector, useDispatch } from 'react-redux'
export default function Counter() {
  const count = useSelector((state) => state)
  const dispatch = useDispatch()
  return (
    <div>
      <div>Count: {count}</div>
      <button onClick={() => dispatch({ type: 'Increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'Decrement' })}>Increment</button>
    </div>
  )
}
