import { useState } from 'react'
import Chat from './components/Chat'
import UserForm from './components/UserForm'
import './App.css'

function App() {
  const [username, setUsername] = useState('')
  
  return (
    <div className="app">
      {!username ? (
        <UserForm onSubmit={setUsername} />
      ) : (
        <Chat username={username} />
      )}
    </div>
  )
}

export default App
