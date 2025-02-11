# Django Project Management System

A Django-based project management system with user authentication and project tracking features.

## Features

- User authentication and authorization
- Client and project management
- Automatic tracking of project creation by users
- RESTful API endpoints for integration

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shaikhtausif7557/management_system.git
   cd management_system
   ```

2. **Create and activate a virtual environment:**

On Windows:

```BASH

python -m venv venv
.\venv\Scripts\activate
```

On macOS/Linux:

```BASH

python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up the database:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

6. **Run the development server:**
```bash
python manage.py runserver
```

## Usage:

- Access the admin panel at /admin to manage users and projects.
- Use the API endpoints to interact with clients and projects.
- Log in to view and manage your assigned projects.
- API Endpoints
- GET /clients/: List all clients
- POST /clients/: Create a new client
- GET /projects/: List all projects
- POST /projects/: Create a new project
- GET /users/: List all users

