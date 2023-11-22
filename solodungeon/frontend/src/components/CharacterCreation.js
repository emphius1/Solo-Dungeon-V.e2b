import React, { useState } from 'react';
import { characterSchema } from '../schemas/characterSchema';

const CharacterCreation = () => {
  const [character, setCharacter] = useState(characterSchema);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setCharacter({ ...character, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // TODO: Implement the function to send character data to the backend
    console.log('Character Created:', character);
    // Emit the CharacterCreated message to the backend
  };

  return (
    <div id="character-creation-form">
      <h2>Create Your Character</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={character.name}
          onChange={handleChange}
          required
        />

        <label htmlFor="race">Race:</label>
        <select
          id="race"
          name="race"
          value={character.race}
          onChange={handleChange}
          required
        >
          {/* Options should be populated based on D&D races */}
        </select>

        <label htmlFor="class">Class:</label>
        <select
          id="class"
          name="class"
          value={character.class}
          onChange={handleChange}
          required
        >
          {/* Options should be populated based on D&D classes */}
        </select>

        {/* Additional character attributes go here */}

        <button type="submit">Create Character</button>
      </form>
    </div>
  );
};

export default CharacterCreation;