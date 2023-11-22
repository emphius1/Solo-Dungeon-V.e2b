# Technology Stack

## Frontend Development

### Core Technologies
- **React**: Utilized for building the user interface, leveraging its component-based architecture for maintainability and reusability.
- **Redux**: Employed for state management across the React application, ensuring a consistent state across all components.

### Styling
- **CSS**: Standard styling of components with a focus on medieval fantasy themes as defined in `frontend/src/styles/themes/medievalFantasyTheme.css`.
- **Sass**: Used for more complex styling scenarios, allowing for variables, nesting, and mixins to maintain thematic consistency.

### Prototyping Tools
- **Figma**: To create wireframes and prototypes as referenced in `frontend/src/wireframes/` and `frontend/src/prototypes/`.

## Backend Development

### Core Framework
- **Django**: Chosen for its robustness and ease of use in creating complex web applications. It will handle game logic, data handling, and API endpoints.

### Database
- **PostgreSQL**: A powerful, open-source object-relational database system with a strong reputation for reliability, feature robustness, and performance.
- **MongoDB**: A NoSQL database for scenarios requiring high write loads, large storage capacity, and horizontal scalability.

### Database ORM
- **Django ORM**: To interact with the database using Python code instead of SQL.

## GPT Assistants Integration

### AI APIs
- **OpenAI Assistant API**: Integrated for creating AI Assistants with the endpoint `https://api.openai.com/v1/assistants`.
- **OpenAI Chat Completions API**: Implemented for handling subtasks within the AI Assistants' responsibilities using the endpoint `https://api.openai.com/v1/chat/completions`.

## UI/UX Design

### Design Software
- **Adobe XD**: For designing and prototyping user interface components.

## Content Creation and Management

### CMS Framework
- **Strapi**: An open-source headless CMS that will be used to manage game content dynamically.

## AI Dungeon Master

### Conversational AI
- **Rasa**: An open-source machine learning framework for automated text and voice-based conversations.

## Integration and Deployment

### Server
- **Node.js**: To run JavaScript on the server-side, particularly for handling OpenAI API interactions.

### Containerization
- **Docker**: For creating, deploying, and running applications using containers, ensuring consistency across various development and deployment environments.

### Cloud Services
- **AWS**: Amazon Web Services for hosting the application with scalability in mind.
- **Azure**: As an alternative cloud service provider, depending on the specific needs and cost considerations.

## Version Control and Collaboration

### Version Control
- **Git**: For source code management.
- **GitHub**: As a hosting platform for version control and collaboration.

## Continuous Integration/Continuous Deployment (CI/CD)

### CI/CD Tools
- **Jenkins**: An open-source automation server that will help automate the parts of software development related to building, testing, and deploying.
- **GitHub Actions**: For automating workflows directly from the GitHub repository.

## Testing

### Testing Frameworks
- **Jest**: For unit testing the React components.
- **pytest**: A framework that makes it easy to write simple tests for Django backend, yet scales to support complex functional testing.

## Performance Optimization

### Profiling Tools
- **Lighthouse**: For auditing the performance of web applications.
- **Webpack Bundle Analyzer**: To visualize the size of webpack output files with an interactive zoomable treemap.

## Security

### Security Tools
- **OAuth**: For secure API authentication.
- **Helmet**: A collection of middleware functions to help secure Express apps by setting various HTTP headers.

This document outlines the technology stack that will be used to build and deploy the AI-driven single-player D&D experience. The selection of technologies is aligned with the project's ideals of creating an intuitive, engaging, and secure application for D&D enthusiasts.