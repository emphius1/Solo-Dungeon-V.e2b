import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CharacterCreation from '../components/CharacterCreation';
import CharacterManagement from '../components/CharacterManagement';
import CombatInterface from '../components/CombatInterface';
import QuestLog from '../components/QuestLog';
import Map from '../components/Map';
import Journal from '../components/Journal';
import Bestiary from '../components/Bestiary';
import NPCRelationships from '../components/NPCRelationships';
import '../styles/themes/medievalFantasyTheme.css';

const UIPrototypes = () => {
  return (
    <Router>
      <Switch>
        <Route path="/character-creation" component={CharacterCreation} />
        <Route path="/character-management" component={CharacterManagement} />
        <Route path="/combat-interface" component={CombatInterface} />
        <Route path="/quest-log" component={QuestLog} />
        <Route path="/map" component={Map} />
        <Route path="/journal" component={Journal} />
        <Route path="/bestiary" component={Bestiary} />
        <Route path="/npc-relationships" component={NPCRelationships} />
      </Switch>
    </Router>
  );
};

export default UIPrototypes;