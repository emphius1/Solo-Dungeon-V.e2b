# Goals: A Text-Based RPG Powered by GPT-4-0613

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Mechanics](#game-mechanics)
5. [AI Dungeon Master](#ai-dungeon-master)
6. [Customization and Modding](#customization-and-modding)
7. [Contribution Guidelines](#contribution-guidelines)
8. [Changelog](#changelog)

## Introduction
Goals is a comprehensive text-based RPG where a chain of GPT-4-0613 models collaboratively function as the Dungeon Master. The AI not only guides players through generated quests, story arcs, and encounters, but also serves as an internal sysadmin responsible for backend operations. The game offers a robust save-load system, dynamic content creation, customization settings, external modding support, and content filtering for age-appropriateness.

## Installation
To install the game, clone the repository and install the dependencies listed in `requirements.txt`.

## How to Play
After installation, run `core.py` to start the game. Follow the prompts to create your character and begin your adventure. Your actions in the game are processed by the AI Dungeon Master, which generates appropriate responses and guides the narrative.

## Game Mechanics
The game mechanics are managed by several scripts in the `/game` directory. `actions.py` scripts the possible actions a player can take, `character.py` manages character creation, progression, stats, and inventory, and `lore.py` creates and manages in-depth lore to add depth to the game.

## AI Dungeon Master
The AI Dungeon Master is powered by GPT-4-0613 and is integrated into the game through several scripts in the `/gpt` directory. `model_integration.py` establishes a connection to the AI model, `prompts.py` engineers system prompts for the AI, and `tools.py` implements various tools for the AI to use.

## Customization and Modding
Players can tweak game preferences through `settings.py` in the `/utils` directory. The game also supports external modding, allowing external content to be added and integrated seamlessly.

## Contribution Guidelines
For information on how to contribute to the project, please refer to `contribution_guidelines.md`.

## Changelog
For a detailed list of updates and changes, please refer to `changelog.md`.