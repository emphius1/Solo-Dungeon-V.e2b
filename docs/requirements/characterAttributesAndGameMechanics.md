# Character Attributes and Game Mechanics

This document outlines the detailed requirements for character attributes and game mechanics for the D&D-inspired game. These attributes and mechanics are integral to the character creation and management process and will be used throughout the game to ensure a consistent and engaging player experience.

## Character Attributes

The following attributes are essential for character creation and will be managed through the `frontend/src/components/CharacterCreation.js` and `frontend/src/components/CharacterManagement.js` components:

- **Strength (STR):** Determines the character's physical power.
- **Dexterity (DEX):** Affects the character's agility and reflexes.
- **Constitution (CON):** Represents the character's health and stamina.
- **Intelligence (INT):** Measures the character's reasoning and memory.
- **Wisdom (WIS):** Reflects the character's perception and insight.
- **Charisma (CHA):** Influences the character's ability to interact effectively with others.

Each attribute will be represented by an integer value, typically ranging from 3 to 18, as per standard D&D rules.

## Skills

Skills are derived from character attributes and will be used in various game mechanics. They include but are not limited to:

- **Acrobatics (DEX):** For performing stunts, dives, rolls, and flips.
- **Arcana (INT):** Knowledge of magic, its lore, and the arcane.
- **Athletics (STR):** Covers climbing, jumping, and swimming activities.
- **Deception (CHA):** The art of lying and misleading others.
- **History (INT):** Knowledge about historical events and legendary figures.
- **Insight (WIS):** The ability to read people and situations.
- **Intimidation (CHA):** The power to influence others through threats.

## Game Mechanics

Game mechanics will be handled by the backend, specifically through `backend/game_logic/gameStateHandler.py`, `backend/game_logic/playerProgressHandler.py`, and `backend/game_logic/gameMechanicsHandler.py`. The mechanics include:

- **Combat Rules:** Turn-based system using attributes and skills to determine the outcomes of attacks, defense, and special abilities.
- **Skill Checks:** When a character attempts an action, a skill check is made by rolling a 20-sided die (d20) and adding relevant skill modifiers.
- **Equipment Management:** Characters can acquire and manage an inventory of items that affect their attributes and skills.

## Integration with Backend

The character attributes and game mechanics will be stored and managed by the backend. The database schema for characters will be defined in `backend/database/models/characterModel.py` using the `CharacterSchema`, which includes fields for all attributes and skills.

## Conclusion

The character attributes and game mechanics are foundational to the game's design and play a critical role in the player's experience. They will be consistently applied across all components of the game, ensuring that the game adheres to the project's ideals and provides an authentic D&D experience.