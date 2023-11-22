import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { characterSchema } from '../shared/schemas';

const CharacterManagement = () => {
  const [characters, setCharacters] = useState([]);
  const [selectedCharacter, setSelectedCharacter] = useState(null);

  useEffect(() => {
    // Fetch characters from the backend
    axios.get('/api/characters')
      .then(response => {
        setCharacters(response.data);
      })
      .catch(error => {
        console.error('Error fetching characters:', error);
      });
  }, []);

  const handleSelectCharacter = (characterId) => {
    const character = characters.find(c => c.id === characterId);
    setSelectedCharacter(character);
  };

  const handleUpdateCharacter = (updatedCharacter) => {
    axios.put(`/api/characters/${updatedCharacter.id}`, updatedCharacter)
      .then(response => {
        setCharacters(characters.map(c => c.id === updatedCharacter.id ? response.data : c));
        setSelectedCharacter(response.data);
      })
      .catch(error => {
        console.error('Error updating character:', error);
      });
  };

  const handleDeleteCharacter = (characterId) => {
    axios.delete(`/api/characters/${characterId}`)
      .then(() => {
        setCharacters(characters.filter(c => c.id !== characterId));
        setSelectedCharacter(null);
      })
      .catch(error => {
        console.error('Error deleting character:', error);
      });
  };

  return (
    <div id="character-management-container">
      <h2>Character Management</h2>
      <div>
        {characters.map(character => (
          <div key={character.id}>
            <button onClick={() => handleSelectCharacter(character.id)}>
              {character.name}
            </button>
          </div>
        ))}
      </div>
      {selectedCharacter && (
        <div>
          <h3>Edit Character</h3>
          {/* Character editing form or component would go here */}
          {/* This form would use handleUpdateCharacter for updates */}
        </div>
      )}
      {selectedCharacter && (
        <button onClick={() => handleDeleteCharacter(selectedCharacter.id)}>
          Delete Character
        </button>
      )}
    </div>
  );
};

export default CharacterManagement;