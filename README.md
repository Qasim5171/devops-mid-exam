221026
Muhammad Qasim

### `README.md`

```markdown
# DevOps Lab mid with Docker Compose and Git Workflow

## Overview

This project demonstrates a simple web application with both frontend and backend services, set up using Docker Compose. The backend is a Flask API that interacts with a PostgreSQL database and a Redis cache. The frontend is a static HTML/CSS/JavaScript page served via Nginx.

### Project Structure

```
my-devops-project/
├── .env                         # Environment variables file
├── .gitignore                   # Git ignore file (including .env)
├── docker-compose.yml           # Docker Compose configuration
├── README.md                    # Project documentation
├── git_setup.txt                # Documentation of Git commands and workflow
├── backend/                     # Backend code for Flask API
│   ├── app.py                   # Flask API code
│   ├── Dockerfile               # Dockerfile for backend
│   └── requirements.txt         # Python dependencies for backend
├── frontend/                    # Frontend code
│   ├── index.html               # Basic HTML file
│   ├── style.css                # Basic CSS file
│   └── script.js                # JavaScript file for frontend
└── .github/
    └── workflows/
        └── docker-build.yml     # GitHub Action for Docker build (optional)
```

## Services

### 1. **Database Service**
   - Uses PostgreSQL to store messages.
   - Automatically initializes a table `messages` and inserts a default message on first run.

### 2. **Cache Service**
   - Uses Redis to cache the message from the database for faster retrieval.
   - Sets an expiry of 60 seconds on cached messages to ensure fresh data.

### 3. **Backend API Service**
   - A simple Flask API that retrieves a message from the database.
   - The message is cached in Redis for improved performance.
   - Endpoint: `GET /api/message` – Returns a message, either from the cache or the database.

### 4. **Frontend Service**
   - A static webpage served by Nginx.
   - Makes a call to the backend API to retrieve the message and display it on the webpage.

## Setup and Running the Project

### Step 1: Configure Environment Variables

1. Create a `.env` file in the project root with the following contents:

   ```plaintext
   POSTGRES_USER=myusername
   POSTGRES_PASSWORD=mypassword
   POSTGRES_DB=mydatabase
   ```

2. Make sure `.env` is added to `.gitignore` to keep it from being committed to the repository.

### Step 2: Start the Services with Docker Compose

1. Ensure Docker is installed and running on your machine.
2. Run the following command to start all services:

   ```bash
   docker-compose up --build
   ```

3. Access the services:
   - **Frontend**: [http://localhost:8080](http://localhost:8080)
   - **Backend API**: [http://localhost:5000/api/message](http://localhost:5000/api/message)

### Step 3: Stop the Services

To stop and remove all running containers, use:

```bash
docker-compose down
```

## Git Branching Workflow

### Branches Used

- **main**: Stable, production-ready code.
- **develop**: Active development branch.
- **feature/database-service**: Branch for adding and testing database-related features.
- **feature/cache-service**: Branch for adding and testing caching features.

### Git Workflow

1. **Create and switch to feature branches** for each service to isolate development.
2. **Merge feature branches** into `develop` once features are tested.
3. **Resolve conflicts** in the code if any arise during the merging process.
4. **Create a pull request** from `develop` to `main` for review and approval.

## GitHub Actions (Optional)

This project includes an optional GitHub Action that automatically builds Docker images when changes are pushed to `main`.

- The GitHub Action is defined in `.github/workflows/docker-build.yml`.

## Environment Variable Management

Environment variables are stored in the `.env` file for secure configuration of sensitive information like database credentials. The `.env` file is excluded from Git version control by adding it to `.gitignore`.

---

## Project Status

This is a basic setup for demonstration purposes. Additional features can be added, such as user authentication, advanced caching strategies, or more complex frontend interactions.


##Screen shots

![image](https://github.com/user-attachments/assets/1b065f64-d348-4f67-9d7a-34ed9d95f2b8)


![image](https://github.com/user-attachments/assets/f67e71c9-a480-492f-b85c-9da5a33281c6)



![image](https://github.com/user-attachments/assets/61e10790-c1a3-4cd7-a321-03d194f60c59)










---



