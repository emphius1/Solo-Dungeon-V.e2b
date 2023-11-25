import React, { useState } from 'react';
import { characterAttributes, themeStyles } from '../styles/themes/medievalFantasyTheme.css';
import { createCharacter } from '../components/CharacterManagement';

const CharacterCreationPrototype = () => {
  const [characterData, setCharacterData] = useState({
    name: '',
    attributes: {
      strength: 0,
      intelligence: 0,
      dexterity: 0,
    },
    skills: [],
    equipment: [],
  });

  const handleAttributeChange = (attribute, value) => {
    setCharacterData({
      ...characterData,
      attributes: {
        ...characterData.attributes,
        [attribute]: value,
      },
    });
  };

  const handleSkillChange = (skill) => {
    if (characterData.skills.includes(skill)) {
      setCharacterData({
        ...characterData,
        skills: characterData.skills.filter((s) => s !== skill),
      });
    } else {
      setCharacterData({
        ...characterData,
        skills: [...characterData.skills, skill],
      });
    }
  };

  const handleEquipmentChange = (item) => {
    if (characterData.equipment.includes(item)) {
      setCharacterData({
        ...characterData,
        equipment: characterData.equipment.filter((i) => i !== item),
      });
    } else {
      setCharacterData({
        ...characterData,
        equipment: [...characterData.equipment, item],
      });
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    createCharacter(characterData);
  };

  return (
    <div id={characterCreationFormId} className={themeStyles}>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          value={characterData.name}
          onChange={(e) => setCharacterData({ ...characterData, name: e.target.value })}
        />

        <div className="attributes">
          {Object.keys(characterAttributes).map((attribute) => (
            <div key={attribute}>
              <label htmlFor={attribute}>{attribute}:</label>
              <input
                type="number"
                id={attribute}
                value={characterData.attributes[attribute]}
                onChange={(e) => handleAttributeChange(attribute, parseInt(e.target.value))}
              />
            </div>
          ))}
        </div>

        <div className="skills">
          {/* Skills checkboxes would be generated here based on gameMechanics */}
        </div>

        <div className="equipment">
          {/* Equipment checkboxes would be generated here based on contentData */}
        </div>

        <button type="submit">Create Character</button>
      </form>
    </div>
  );
};

export default CharacterCreationPrototype;