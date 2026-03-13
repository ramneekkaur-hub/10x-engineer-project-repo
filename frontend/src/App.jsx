import React, { useState } from 'react';
import './App.css';
import PromptForm from './components/prompts/PromptForm';
import PromptList from './components/prompts/PromptList'; // Added the PromptList import

function App() {
  const [isCreatingNew, setIsCreatingNew] = useState(false); // Managing new prompt creation
  const [searchQuery, setSearchQuery] = useState(''); // Managing search
  const [successMessage, setSuccessMessage] = useState(''); // Managing success messages

  // Example state and logo imports - not used in the new structure
  // const [count, setCount] = useState(0)
  // import reactLogo from './assets/react.svg'
  // import viteLogo from '/vite.svg'

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleFormSuccess = (message) => {
    setIsCreatingNew(false);
    setSuccessMessage(message);
    // Clear success message after a few seconds
    setTimeout(() => setSuccessMessage(''), 3000);
  };

  const handleSuccess = () => {
    console.log('Prompt saved successfully');
    // Add logic to refresh prompt list or navigate after success
  };

  return (
    // Original div structure and comments remain largely the same
    <>
      {/* The Vite and React logos with links - the commented out sections */}
      {/* <div> */}
        {/* <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a> */}
        {/* <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a> */}
      {/* </div> */}
      {/* <h1>Vite + React</h1> */}
      {/* <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div> */}
      {/* <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p> */}

      <div className="app-container">
        <header className="app-header">
          <h1 className="app-title">Prompt Management</h1>
        </header>
        <main className="app-main">
          {successMessage && <div className="success-message">{successMessage}</div>}

          <div className="controls">
            <button className="action-button" onClick={() => setIsCreatingNew(true)}>New Prompt</button>
            <input
              type="text"
              className="search-input"
              placeholder="Search prompts"
              value={searchQuery}
              onChange={handleSearchChange}
            />
          </div>

          {isCreatingNew && <PromptForm onSuccess={(message) => handleFormSuccess(message || 'Prompt created successfully!')} />}
          <PromptList
            searchQuery={searchQuery}
            onPromptUpdate={handleFormSuccess}
          />
        </main>
      </div>
    </>
  );
}

export default App;

