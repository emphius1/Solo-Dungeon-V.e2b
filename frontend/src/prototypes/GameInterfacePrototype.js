import React from 'react';
import CharacterCreation from '../components/CharacterCreation';
import CharacterManagement from '../components/CharacterManagement';
import CombatInterface from '../components/CombatInterface';
import QuestLog from '../components/QuestLog';
import Map from '../components/Map';
import Journal from '../components/Journal';
import Bestiary from '../components/Bestiary';
import NPCRelationships from '../components/NPCRelationships';
import '../styles/themes/medievalFantasyTheme.css';

class GameInterfacePrototype extends React.Component {
  render() {
    return (
      <div className="game-interface" style={themeStyles}>
        <CharacterCreation id={characterCreationFormId} />
        <CharacterManagement id={characterManagementContainerId} />
        <CombatInterface id={combatInterfaceId} />
        <QuestLog id={questLogId} />
        <Map id={mapContainerId} />
        <Journal id={journalContainerId} />
        <Bestiary id={bestiaryContainerId} />
        <NPCRelationships id={npcRelationshipsContainerId} />
      </div>
    );
  }
}

export default GameInterfacePrototype;