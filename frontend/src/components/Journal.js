import React, { useState, useEffect } from 'react';
import { addJournalEntry, JournalEntryAdded } from '../sharedDependencies';
import './styles/themes/medievalFantasyTheme.css';

const Journal = () => {
  const [journalEntries, setJournalEntries] = useState([]);
  const [newEntry, setNewEntry] = useState('');

  useEffect(() => {
    // TODO: Fetch existing journal entries from the backend
  }, []);

  const handleNewEntryChange = (event) => {
    setNewEntry(event.target.value);
  };

  const handleAddEntry = () => {
    if (newEntry.trim() !== '') {
      const updatedEntries = [...journalEntries, newEntry];
      setJournalEntries(updatedEntries);
      setNewEntry('');
      // TODO: Send new entry to the backend
      // Emit an event/message that a new journal entry has been added
      document.dispatchEvent(new CustomEvent(JournalEntryAdded, { detail: newEntry }));
    }
  };

  return (
    <div id="journalContainerId" className="journal-container medieval-fantasy-theme">
      <h2>Journal</h2>
      <div className="journal-entries">
        {journalEntries.map((entry, index) => (
          <div key={index} className="journal-entry">
            {entry}
          </div>
        ))}
      </div>
      <textarea
        value={newEntry}
        onChange={handleNewEntryChange}
        placeholder="Write your adventure..."
        className="journal-new-entry"
      />
      <button onClick={handleAddEntry} className="journal-add-button">
        Add Entry
      </button>
    </div>
  );
};

export default Journal;