import React, { useState, useEffect } from 'react';
import { journalSchema } from '../sharedDependencies';
import './styles/main.css';

const Journal = () => {
  const [journalEntries, setJournalEntries] = useState([]);

  useEffect(() => {
    // Placeholder for fetching journal entries from the backend
    // In a real application, this would be replaced with an API call
    const fetchJournalEntries = async () => {
      // const response = await fetch('/api/journal');
      // const data = await response.json();
      // setJournalEntries(data);
    };

    fetchJournalEntries();
  }, []);

  const addJournalEntry = (entry) => {
    // Placeholder for adding a journal entry to the backend
    // In a real application, this would be replaced with an API call
    const postJournalEntry = async () => {
      // const response = await fetch('/api/journal', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   body: JSON.stringify(entry),
      // });
      // if (response.ok) {
      //   fetchJournalEntries();
      // }
    };

    postJournalEntry();
  };

  const handleJournalSubmit = (event) => {
    event.preventDefault();
    const entry = event.target.elements[journalSchema.entryField].value;
    if (entry) {
      addJournalEntry({ entry });
      event.target.reset();
    }
  };

  return (
    <div className="journal-container">
      <h2>Journal</h2>
      <form id="journal-entry-form" onSubmit={handleJournalSubmit}>
        <textarea id={journalSchema.entryField} placeholder="Enter your journal entry here..." />
        <button type="submit">Add Entry</button>
      </form>
      <div className="journal-entries">
        {journalEntries.map((entry, index) => (
          <div key={index} className="journal-entry">
            <p>{entry}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Journal;