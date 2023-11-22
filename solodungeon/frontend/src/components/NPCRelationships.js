import React, { useState, useEffect } from 'react';
import { npcRelationshipSchema } from '../sharedDependencies';

const NPCRelationships = () => {
  const [npcRelationships, setNpcRelationships] = useState([]);

  useEffect(() => {
    // Fetch NPC relationships from the backend when the component mounts
    const fetchNPCRelationships = async () => {
      try {
        const response = await fetch('/api/npc-relationships');
        const data = await response.json();
        setNpcRelationships(data);
      } catch (error) {
        console.error('Failed to fetch NPC relationships:', error);
      }
    };

    fetchNPCRelationships();
  }, []);

  const updateNPCRelationship = async (npcId, newRelationship) => {
    try {
      const response = await fetch(`/api/npc-relationships/${npcId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newRelationship),
      });

      if (response.ok) {
        setNpcRelationships(npcRelationships.map(npc => 
          npc.id === npcId ? { ...npc, ...newRelationship } : npc
        ));
      }
    } catch (error) {
      console.error('Failed to update NPC relationship:', error);
    }
  };

  return (
    <div id="npc-relationships-chart">
      <h2>NPC Relationships</h2>
      <ul>
        {npcRelationships.map(npc => (
          <li key={npc.id}>
            <h3>{npc.name}</h3>
            <p>Relationship: {npc.relationship}</p>
            <button onClick={() => updateNPCRelationship(npc.id, { relationship: 'Friend' })}>
              Befriend
            </button>
            <button onClick={() => updateNPCRelationship(npc.id, { relationship: 'Foe' })}>
              Antagonize
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NPCRelationships;