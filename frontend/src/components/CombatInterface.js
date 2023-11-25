import React, { useState, useEffect } from 'react';
import { themeStyles } from '../styles/themes/medievalFantasyTheme.css';
import { handleCombat, fetchAssistantAction } from '../helpers/assistantSubtaskHelper';

const CombatInterface = () => {
  const [combatLog, setCombatLog] = useState([]);
  const [currentAction, setCurrentAction] = useState('');

  useEffect(() => {
    // Fetch initial combat state or setup
  }, []);

  const performAction = async (action) => {
    setCurrentAction(action);
    const combatOutcome = await handleCombat(action);
    setCombatLog([...combatLog, combatOutcome]);
    
    // Fetch next possible actions from the AI Dungeon Master
    const nextActions = await fetchAssistantAction('fetchNextCombatActions');
    // Handle the response and update the UI accordingly
  };

  return (
    <div id={combatInterfaceId} className={themeStyles}>
      <h2>Combat Interface</h2>
      <div className="combat-actions">
        {/* Buttons for combat actions */}
        <button onClick={() => performAction('attack')}>Attack</button>
        <button onClick={() => performAction('defend')}>Defend</button>
        <button onClick={() => performAction('useItem')}>Use Item</button>
        <button onClick={() => performAction('flee')}>Flee</button>
      </div>
      <div className="combat-log">
        <h3>Combat Log</h3>
        <ul>
          {combatLog.map((logEntry, index) => (
            <li key={index}>{logEntry}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CombatInterface;