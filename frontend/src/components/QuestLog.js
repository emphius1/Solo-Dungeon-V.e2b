import React, { useState, useEffect } from 'react';
import { apiEndpoints } from '../shared/apiEndpoints';
import { questLogId, QuestLogUpdated } from '../shared/sharedDependencies';
import './styles/themes/medievalFantasyTheme.css';

const QuestLog = () => {
  const [quests, setQuests] = useState([]);
  const [selectedQuest, setSelectedQuest] = useState(null);

  useEffect(() => {
    // Fetch quests from the backend or local storage
    fetchQuests();
  }, []);

  const fetchQuests = async () => {
    try {
      const response = await fetch(apiEndpoints.questLogEndpoint);
      const data = await response.json();
      setQuests(data.quests);
    } catch (error) {
      console.error('Failed to fetch quests:', error);
    }
  };

  const handleQuestSelection = (questId) => {
    const quest = quests.find(q => q.id === questId);
    setSelectedQuest(quest);
    document.dispatchEvent(new CustomEvent(QuestLogUpdated, { detail: quest }));
  };

  return (
    <div id={questLogId} className="quest-log-container medieval-fantasy-theme">
      <h2>Quest Log</h2>
      <ul className="quest-list">
        {quests.map(quest => (
          <li key={quest.id} className={`quest-item ${selectedQuest && selectedQuest.id === quest.id ? 'selected' : ''}`} onClick={() => handleQuestSelection(quest.id)}>
            {quest.title}
          </li>
        ))}
      </ul>
      {selectedQuest && (
        <div className="quest-details">
          <h3>{selectedQuest.title}</h3>
          <p>{selectedQuest.description}</p>
          <p>Status: {selectedQuest.status}</p>
        </div>
      )}
    </div>
  );
};

export default QuestLog;