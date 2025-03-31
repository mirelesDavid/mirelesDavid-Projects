import { useState } from 'react';
import './UserForm.css';

const UserForm = ({ onSubmit }) => {
  const [username, setUsername] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username.trim()) {
      onSubmit(username);
    }
  };

  return (
    <div className="user-form-container">
      <div className="user-form">
        <h2>Join the Chat</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Enter your name:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Your name"
              autoFocus
              required
            />
          </div>
          <button type="submit">Join Chat</button>
        </form>
      </div>
    </div>
  );
};

export default UserForm; 