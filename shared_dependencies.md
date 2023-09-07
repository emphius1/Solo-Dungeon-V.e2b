# Shared Dependencies

This document outlines the shared dependencies across the various modules of our text-based RPG game. These dependencies are crucial for the seamless interaction between different parts of the game.

## Database Schema

The structure of the database including tables for characters, quests, AI-generated content, and player saves is shared across the database files (`db_init.py`, `db_ops.py`, `cache.py`) and the game files (`core.py`, `actions.py`, `character.py`, `lore.py`).

## GPT-4-0613 Model

The AI model is shared across the GPT integration files (`model_integration.py`, `prompts.py`, `tools.py`, `context_manager.py`, `dynamic_content.py`) and the game files (`core.py`, `actions.py`).

## Game Data

The game data including player inputs, AI responses, and game state is shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`), utility files (`error_handlers.py`, `spell_lookup.py`, `campaign_manager.py`, `save_load.py`, `settings.py`, `content_filter.py`), and data management file (`data_management.py`).

## Error Handling Functions

The functions for handling errors are shared across all the files.

## Spell Lookup Functions

The functions for spell lookups are shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`) and the utility file (`spell_lookup.py`).

## Save and Load Functions

The functions for saving and loading game state are shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`), utility file (`save_load.py`), and data management file (`data_management.py`).

## Settings

The game settings are shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`), utility file (`settings.py`), and data management file (`data_management.py`).

## Content Filter Functions

The functions for content filtering are shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`), utility file (`content_filter.py`), and data management file (`data_management.py`).

## Mod Support Functions

The functions for supporting mods are shared across the game files (`core.py`, `actions.py`, `character.py`, `lore.py`) and the mod support file (`mod_support.py`).

## Test Functions

The functions for testing are shared across all the files and the test files (`unit_tests.py`, `feedback.py`).

## Documentation

The documentation is shared across all the files and the documentation files (`README.md`, `contribution_guidelines.md`, `changelog.md`).

## Requirements

The requirements are shared across all the files and the requirements file (`requirements.txt`).