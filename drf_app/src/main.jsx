import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import EmployeeList from './EmployeeList'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    HELLO
    <EmployeeList />
  </StrictMode>,
)
