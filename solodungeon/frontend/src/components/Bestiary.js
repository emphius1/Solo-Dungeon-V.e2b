import React, { useState, useEffect } from 'react';
import { bestiarySchema } from '../schemas';
import './styles/main.css';

const Bestiary = () => {
  const [bestiary, setBestiary] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Placeholder for fetching bestiary data from the backend
    const fetchBestiary = async () => {
      try {
        // Replace with actual API endpoint
        const response = await fetch('/api/bestiary');
        const data = await response.json();
        setBestiary(data);
      } catch (error) {
        console.error('Failed to fetch bestiary:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchBestiary();
  }, []);

  const renderBestiaryEntry = (entry) => (
    <div key={entry.id} className="bestiary-entry">
      <h3>{entry.name}</h3>
      <p>{entry.description}</p>
      {/* Additional details can be added here */}
    </div>
  );

  return (
    <div id="bestiary-list" className="bestiary-container">
      <h2>Bestiary</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        bestiary.map((entry) => renderBestiaryEntry(entry))
      )}
    </div>
  );
};

export default Bestiary;