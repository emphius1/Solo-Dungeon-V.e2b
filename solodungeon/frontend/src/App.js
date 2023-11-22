import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CharacterCreation from './components/CharacterCreation';
import CharacterManagement from './components/CharacterManagement';
import Inventory from './components/Inventory';
import Combat from './components/Combat';
import QuestLog from './components/QuestLog';
import Map from './components/Map';
import Journal from './components/Journal';
import Bestiary from './components/Bestiary';
import NPCRelationships from './components/NPCRelationships';
import './styles/main.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/character-creation" component={CharacterCreation} />
          <Route path="/character-management" component={CharacterManagement} />
          <Route path="/inventory" component={Inventory} />
          <Route path="/combat" component={Combat} />
          <Route path="/quest-log" component={QuestLog} />
          <Route path="/map" component={Map} />
          <Route path="/journal" component={Journal} />
          <Route path="/bestiary" component={Bestiary} />
          <Route path="/npc-relationships" component={NPCRelationships} />
          <Route path="/" exact component={CharacterCreation} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;