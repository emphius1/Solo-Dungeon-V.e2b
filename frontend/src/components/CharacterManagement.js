import React, { useState, useEffect } from 'react';
import { characterAttributes, updateCharacter, CharacterUpdateSuccess } from '../sharedDependencies';
import CharacterForm from './CharacterForm';

const CharacterManagement = () => {
  const [characters, setCharacters] = useState([]);
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  const [editMode, setEditMode] = useState(false);

  useEffect(() => {
    // Fetch characters from the backend and set them in state
    // This is a placeholder for the actual API call
    fetch('/api/characters')
      .then(response => response.json())
      .then(data => setCharacters(data))
      .catch(error => console.error('Error fetching characters:', error));
  }, []);

  const handleEditClick = (character) => {
    setSelectedCharacter(character);
    setEditMode(true);
  };

  const handleCharacterUpdate = (updatedCharacter) => {
    updateCharacter(updatedCharacter)
      .then(() => {
        setCharacters(characters.map((char) => (char.id === updatedCharacter.id ? updatedCharacter : char)));
        setSelectedCharacter(null);
        setEditMode(false);
        alert(CharacterUpdateSuccess);
      })
      .catch(error => console.error('Error updating character:', error));
  };

  const handleCancelEdit = () => {
    setSelectedCharacter(null);
    setEditMode(false);
  };

  return (
    <div id={characterManagementContainerId}>
      <h1>Character Management</h1>
      {editMode ? (
        <CharacterForm
          character={selectedCharacter}
          characterAttributes={characterAttributes}
          onSave={handleCharacterUpdate}
          onCancel={handleCancelEdit}
        />
      ) : (
        <div>
          <h2>Your Characters</h2>
          <ul>
            {characters.map(character => (
              <li key={character.id}>
                {character.name}
                <button onClick={() => handleEditClick(character)}>Edit</button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default CharacterManagement;