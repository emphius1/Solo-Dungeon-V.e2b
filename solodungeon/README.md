# SoloDungeon

SoloDungeon is a hybrid React and Django application that offers a unique single-player experience of 5e Dungeons & Dragons. It leverages advanced Large Language Model (LLM) agents to serve as the Dungeon Master, providing a rich narrative and interactive gameplay.

## Features

- **Character Creation & Management**: Players can create and manage their D&D characters.
- **Inventory System**: A detailed inventory interface for managing player items.
- **Combat Mechanics**: Real-time combat system with strategic gameplay.
- **Quest Logging**: Players can track their quests and objectives.
- **Interactive Maps**: Explore the world with interactive maps.
- **Journaling**: Keep a log of adventures and notes within the game.
- **Bestiary**: A compendium of creatures encountered during the game.
- **NPC Relationships**: Track and develop relationships with non-player characters.
- **AI Dungeon Master**: Engage with an AI-powered Dungeon Master for a dynamic narrative.
- **Responsive UI Design**: Aesthetic that resonates with the medieval fantasy of D&D.

## Tech Stack

- **Frontend**: React.js
- **Backend**: Django
- **Database**: PostgreSQL or MongoDB
- **AI Integration**: Python-based LLM agents
- **Testing**: Jest for frontend, PyTest for backend
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Hosting**: AWS or Azure

## Getting Started

To get started with SoloDungeon, clone the repository and follow the setup instructions for both frontend and backend services.

```bash
git clone https://github.com/your-repository/solodungeon.git
cd solodungeon
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```

## Testing

To run the tests for the frontend:

```bash
cd frontend
npm test
```

To run the tests for the backend:

```bash
cd backend
pytest
```

## Deployment

SoloDungeon can be deployed using Docker and the provided Dockerfile and docker-compose.yml files.

```bash
docker-compose up --build
```

## Contributing

We welcome contributions! Please read the `CONTRIBUTING.md` file for guidelines on how to submit pull requests.

## License

SoloDungeon is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Dungeons & Dragons, Wizards of the Coast, and all related terms are trademarks of Wizards of the Coast LLC.
- This project is not affiliated with, endorsed, sponsored, or specifically approved by Wizards of the Coast LLC.