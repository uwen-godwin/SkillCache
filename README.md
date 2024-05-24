# SkillCache Portfolio Project

## Description
SkillCache is a portfolio platform for tech professionals to showcase their skills and projects. This project includes a frontend built with HTML, CSS, and JavaScript, a backend using Flask, and a PostgreSQL database.

## Architecture
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: PostgreSQL
- **Version Control**: Git
- **Deployment**: GitHub Pages (frontend), Flask application (backend)

## Data Flow
1. User interacts with the frontend UI.
2. Frontend sends requests to the Flask backend.
3. Flask processes requests and interacts with the PostgreSQL database.
4. Database retrieves or stores user data.
5. Backend sends a response back to the frontend.

## APIs and Methods
### Web Client to Web Server Communication
- `/api/portfolio`
  - `GET`: Retrieves user's portfolio data.
  - `POST`: Adds or updates user's portfolio information.
- `/api/skills`
  - `GET`: Retrieves user's skills list.
  - `POST`: Adds a new skill to the user's profile.
- `/api/projects`
  - `GET`: Retrieves user's projects list.
  - `POST`: Adds a new project to the user's profile.

### External Client Use
- `SkillCachePortfolio`
  - `retrieve_user_portfolio()`: Retrieves a user's portfolio information.
- `SkillCacheSkills`
  - `add_skill(skill_name)`: Adds a new skill to a user's profile.
- `SkillCacheProjects`
  - `retrieve_user_projects()`: Retrieves a user's projects list.

## User Stories
1. As a tech professional, I want to create a personalized portfolio on SkillCache to showcase my skills and projects to potential employers or clients.
2. As a user, I want to be able to add and update my skills easily on SkillCache.
3. As a tech enthusiast, I want to browse and view other users' portfolios on SkillCache.
4. As a recruiter, I want to search for users based on specific skills or project criteria on SkillCache.
5. As a hiring manager, I want to be able to contact users directly through SkillCache.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/uwen-godwin/SkillCache.git
   cd SkillCache

