import React, { useState } from 'react';
import { characterAttributes, themeStyles } from '../styles/themes/medievalFantasyTheme.css';
import { CharacterSchema } from '../../backend/database/models/characterModel';
import { createCharacter, CharacterCreationSuccess } from '../../backend/helpers/assistantSubtaskHelper';

const CharacterCreation = () => {
  const [character, setCharacter] = useState(new CharacterSchema());

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setCharacter({ ...character, [name]: value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await createCharacter(character);
      alert(CharacterCreationSuccess);
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div id={characterCreationFormId} className={themeStyles}>
      <form onSubmit={handleSubmit}>
        {Object.keys(characterAttributes).map((attribute) => (
          <div key={attribute}>
            <label htmlFor={attribute}>{attribute.charAt(0).toUpperCase() + attribute.slice(1)}:</label>
            <input
              type="number"
              id={attribute}
              name={attribute}
              value={character[attribute]}
              onChange={handleInputChange}
            />
          </div>
        ))}
        <button type="submit">Create Character</button>
      </form>
    </div>
  );
};

export default CharacterCreation;