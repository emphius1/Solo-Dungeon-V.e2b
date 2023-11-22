import React, { useState, useEffect } from 'react';
import { manageNPCRelationships, fetchAssistantAction } from '../helpers/assistantSubtaskHelper';
import '../styles/themes/medievalFantasyTheme.css';

const NPCRelationships = () => {
  const [npcList, setNpcList] = useState([]);
  const [selectedNPC, setSelectedNPC] = useState(null);
  const [relationshipDetails, setRelationshipDetails] = useState('');

  useEffect(() => {
    // Fetch the list of NPCs from the backend or local content data
    // This is a placeholder for actual data fetching logic
    setNpcList([
      { id: 1, name: 'Gandalf the Grey', status: 'Friendly' },
      { id: 2, name: 'Legolas Greenleaf', status: 'Neutral' },
      { id: 3, name: 'Gimli son of Glóin', status: 'Allied' },
    ]);
  }, []);

  const handleNPCSelection = (npcId) => {
    const npc = npcList.find(npc => npc.id === npcId);
    setSelectedNPC(npc);
    fetchRelationshipDetails(npcId);
  };

  const fetchRelationshipDetails = async (npcId) => {
    // Placeholder for fetching relationship details from the backend
    // In a real application, this would be an API call
    const details = await fetchAssistantAction('FetchNPCRelationshipDetails', npcId);
    setRelationshipDetails(details);
  };

  return (
    <div id={npcRelationshipsContainerId} className="npc-relationships-container medievalFantasyTheme">
      <h2>NPC Relationships</h2>
      <ul className="npc-list">
        {npcList.map(npc => (
          <li key={npc.id} className={`npc-item ${selectedNPC && selectedNPC.id === npc.id ? 'selected' : ''}`} onClick={() => handleNPCSelection(npc.id)}>
            {npc.name} - {npc.status}
          </li>
        ))}
      </ul>
      {selectedNPC && (
        <div className="relationship-details">
          <h3>{selectedNPC.name}</h3>
          <p>{relationshipDetails}</p>
        </div>
      )}
    </div>
  );
};

export default NPCRelationships;