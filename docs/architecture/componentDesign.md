# Component Design

This document outlines the modular design of the system, identifying key components and their interactions within the architecture.

## Frontend Components

### Character Creation and Management
- **Component:** `CharacterCreation.js`
- **Responsibilities:** Handles the UI for creating and managing D&D characters.
- **Interactions:** Communicates with `characterModel.py` through `restfulAPI.py` to save and retrieve character data.

### Game Interface Elements
- **Components:** 
  - `CombatInterface.js`
  - `QuestLog.js`
  - `Map.js`
  - `Journal.js`
  - `Bestiary.js`
  - `NPCRelationships.js`
- **Responsibilities:** Each component manages its respective game interface element.
- **Interactions:** Interact with various backend handlers like `gameStateHandler.py`, `playerProgressHandler.py`, and `gameMechanicsHandler.py` for game state updates.

### Design Aesthetics
- **Component:** `medievalFantasyTheme.css`
- **Responsibilities:** Provides styling for all UI components to maintain a consistent medieval fantasy theme.
- **Interactions:** Imported by all React components to ensure thematic consistency.

### Prototyping
- **Components:** 
  - `CharacterCreationPrototype.js`
  - `GameInterfacePrototype.js`
- **Responsibilities:** Prototypes for testing UI design and user interaction.
- **Interactions:** Used for gathering user feedback to refine UI components.

## Backend Components

### Game Logic and Data Handling
- **Components:** 
  - `gameStateHandler.py`
  - `playerProgressHandler.py`
  - `gameMechanicsHandler.py`
- **Responsibilities:** Manage game logic, player progress, and game mechanics.
- **Interactions:** Communicate with database adapters to persist game data.

### Database Integration
- **Components:** 
  - `postgresqlAdapter.py`
  - `mongodbAdapter.py`
- **Responsibilities:** Interface with the selected database to perform CRUD operations.
- **Interactions:** Used by game logic handlers to store and retrieve data.

## GPT Assistants Integration

### Assistants API
- **Component:** `assistantsAPI.py`
- **Responsibilities:** Integrates with OpenAI's Assistant API to create various assistant roles.
- **Interactions:** Calls `assistantSubtaskHelper.py` to handle specific subtasks.

### Assistant Actions
- **Component:** `assistantsOpenAPI.yaml`
- **Responsibilities:** Provides OpenAPI specifications for assistant actions.
- **Interactions:** Used by `assistantsAPI.py` to define and document the capabilities of the assistants.

## GPT-4-1106-preview Integration

### GPT-4-1106-preview API
- **Component:** `gpt4_1106_previewAPI.py`
- **Responsibilities:** Handles interactions with OpenAI's Chat Completions API for dynamic AI tasks.
- **Interactions:** Invoked by `assistantsAPI.py` to perform narrative generation and other AI-driven tasks.

## UI/UX Design

### Accessibility and Thematic Consistency
- **Components:** 
  - `accessibilityGuidelines.js`
  - `thematicElements.js`
- **Responsibilities:** Ensure UI/UX is accessible and thematically consistent with the D&D universe.
- **Interactions:** Guidelines and elements are applied across all frontend components.

## Content Creation and Management

### D&D Content Adapter
- **Component:** `dndContentAdapter.py`
- **Responsibilities:** Manages the integration of D&D content into the game.
- **Interactions:** Works with `contentManagementSystem.py` to update and manage game content.

### Content Management System
- **Component:** `contentManagementSystem.py`
- **Responsibilities:** Provides a system for adding and modifying game content.
- **Interactions:** Used by game designers to input new content into the game.

## Player Interaction with AI Dungeon Master

### Conversational AI
- **Component:** `conversationalAI.py`
- **Responsibilities:** Enables the AI Dungeon Master to engage in natural conversations.
- **Interactions:** Utilizes `adaptiveResponseGenerator.py` to provide contextually appropriate responses.

### Adaptive Responses
- **Component:** `adaptiveResponseGenerator.py`
- **Responsibilities:** Generates AI responses that maintain narrative consistency.
- **Interactions:** Supports `conversationalAI.py` in delivering dynamic dialogue.

## Integration and Deployment

### Frontend-Backend Integration
- **Component:** `frontendBackendIntegrationStrategy.md`
- **Responsibilities:** Outlines the strategy for connecting frontend and backend components.
- **Interactions:** Ensures seamless data exchange and real-time updates between client and server.

### Cloud Hosting and Containerization
- **Components:** 
  - `cloudHostingSetup.md`
  - `dockerContainerizationStrategy.md`
- **Responsibilities:** Details the steps for deployment and hosting of the application.
- **Interactions:** Guides the setup of servers and containerization for scalable deployment.

## Testing and Quality Assurance

### Testing Strategy
- **Component:** `testingStrategy.md`
- **Responsibilities:** Establishes a comprehensive testing plan for the application.
- **Interactions:** Informs developers and QA teams on unit, integration, and user testing protocols.

## Vision Alignment

### Product Vision Statement
- **Component:** `productVisionStatement.md`
- **Responsibilities:** Ensures that the final product aligns with the project's goals.
- **Interactions:** Acts as a guiding document for all development activities to adhere to the project's ideals.

This component design is a living document and will evolve as the project progresses. It serves as a blueprint for developers to understand the system's modular structure and how each component fits into the overall architecture.