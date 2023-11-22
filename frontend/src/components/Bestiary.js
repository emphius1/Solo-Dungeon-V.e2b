import React, { useState, useEffect } from 'react';
import { accessBestiary } from '../helpers/assistantSubtaskHelper';
import { themeStyles } from '../styles/themes/medievalFantasyTheme.css';

const Bestiary = () => {
  const [creatures, setCreatures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    accessBestiary()
      .then(data => {
        setCreatures(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div id="bestiaryContainerId" className={themeStyles}>
      <h1>Bestiary</h1>
      <ul>
        {creatures.map((creature, index) => (
          <li key={index}>
            <h2>{creature.name}</h2>
            <p>{creature.description}</p>
            <div>
              <strong>HP:</strong> {creature.hitPoints}
            </div>
            <div>
              <strong>AC:</strong> {creature.armorClass}
            </div>
            <div>
              <strong>Abilities:</strong> {creature.abilities.join(', ')}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Bestiary;