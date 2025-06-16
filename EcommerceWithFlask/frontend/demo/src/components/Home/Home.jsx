import React, { useState } from 'react'

export default function Home() {
    const [inputUsername, setInputUsername] = useState('');
    const [result, setResult] = useState('');
  
    const getUsername = async () => {
      if (!inputUsername) {
        setResult('Please enter a username.');
        return;
      }
      try {
        const response = await fetch(`http://localhost:7777/username/${inputUsername}`);
        const data = await response.json();
        if (data.status === 'success') {
          setResult(`Hello, ${data.data.username}!`);
        } else {
          setResult('User not found.');
        }
      } catch (error) {
        console.error('Error fetching username:', error);
        setResult('Error fetching data.');
      }
    };
  return (
    <div>
       <input
        type="text"
        placeholder="Enter username"
        value={inputUsername}
        onChange={(e) => setInputUsername(e.target.value)}
        style={{ padding: '8px', width: '200px', marginRight: '10px' }}
      />
      <button onClick={getUsername} style={{ padding: '8px 12px' }}>
        Get User
      </button>
      <h2 style={{ marginTop: '20px' }}>{result}</h2>
    </div>
  )
}
