-- Schema for Dungeons & Dragons Character Management System

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS characters CASCADE;
DROP TABLE IF EXISTS quests CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS game_histories CASCADE;
DROP TABLE IF EXISTS campaign_settings CASCADE;
DROP TABLE IF EXISTS npc_relationships CASCADE;

-- Create table for character attributes
CREATE TABLE characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    strength INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    constitution INTEGER NOT NULL,
    wisdom INTEGER NOT NULL,
    charisma INTEGER NOT NULL,
    equipment TEXT,
    skills TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for quests
CREATE TABLE quests (
    quest_id SERIAL PRIMARY KEY,
    character_id INTEGER REFERENCES characters(character_id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for items
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    type VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for game histories
CREATE TABLE game_histories (
    history_id SERIAL PRIMARY KEY,
    character_id INTEGER REFERENCES characters(character_id),
    event TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for campaign settings
CREATE TABLE campaign_settings (
    setting_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for NPC relationships
CREATE TABLE npc_relationships (
    relationship_id SERIAL PRIMARY KEY,
    character_id INTEGER REFERENCES characters(character_id),
    npc_name VARCHAR(255) NOT NULL,
    relationship_level INTEGER,
    last_interaction TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for faster search
CREATE INDEX idx_character_name ON characters(name);
CREATE INDEX idx_quest_title ON quests(title);
CREATE INDEX idx_item_name ON items(name);
CREATE INDEX idx_npc_name ON npc_relationships(npc_name);

-- Triggers to update 'updated_at' column on data change
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = now();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_characters_modtime
    BEFORE UPDATE ON characters
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_quests_modtime
    BEFORE UPDATE ON quests
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_campaign_settings_modtime
    BEFORE UPDATE ON campaign_settings
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_npc_relationships_modtime
    BEFORE UPDATE ON npc_relationships
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();