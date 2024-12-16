# Project Management Application

## Overview
This is a project management application built with Django and Django REST Framework (DRF) that allows users to register, log in, manage projects, tasks, and comments. It also includes Swagger API documentation for easy access to the API endpoints.

---

## Features
- **User Authentication**: Register, login, and manage users.
- **Project Management**: Create, update, delete, and view projects.
- **Task Management**: Create, update, delete, and view tasks within projects.
- **Comments on Tasks**: Create, update, delete, and view comments for tasks.
- **API Documentation**: Swagger UI to view and test API endpoints.

---

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/project-management.git
cd project-management
2. Set up a virtual environment
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure the database
Make sure to set up your database in settings.py (default SQLite or configure PostgreSQL/MySQL).
Run migrations to create the database tables:
bash
Copy code
python manage.py migrate
5. Create a superuser (optional)
If you want to access the Django admin panel, create a superuser:

bash
Copy code
python manage.py createsuperuser
6. Run the development server
bash
Copy code
python manage.py runserver
API Endpoints
Users
Register User

POST /api/users/register/
Body:
json
Copy code
{
  "username": "user1",
  "email": "user1@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}
Login User

POST /api/users/login/
Body:
json
Copy code
{
  "username": "user1",
  "password": "password123"
}
Response:
json
Copy code
{
  "access_token": "your_access_token"
}
Get User Details

GET /api/users/{id}/
Response:
json
Copy code
{
  "id": 1,
  "username": "user1",
  "email": "user1@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
Update User

PUT /api/users/{id}/
Body:
json
Copy code
{
  "username": "updated_username",
  "email": "updated_email@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
Delete User

DELETE /api/users/{id}/
Response:
json
Copy code
{
  "message": "User deleted successfully"
}
Projects
List Projects

GET /api/projects/
Response:
json
Copy code
[
  {
    "id": 1,
    "name": "Project 1",
    "description": "Description of Project 1",
    "owner": 1,
    "created_at": "2024-12-16T12:00:00Z"
  }
]
Create Project

POST /api/projects/
Body:
json
Copy code
{
  "name": "New Project",
  "description": "Description of new project",
  "owner": 1
}
Retrieve Project

GET /api/projects/{id}/
Response:
json
Copy code
{
  "id": 1,
  "name": "Project 1",
  "description": "Description of Project 1",
  "owner": 1,
  "created_at": "2024-12-16T12:00:00Z"
}
Update Project

PUT /api/projects/{id}/
Body:
json
Copy code
{
  "name": "Updated Project",
  "description": "Updated description",
  "owner": 1
}
Delete Project

DELETE /api/projects/{id}/
Response:
json
Copy code
{
  "message": "Project deleted successfully"
}
Tasks
List Tasks

GET /api/projects/{project_id}/tasks/
Response:
json
Copy code
[
  {
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "status": "To Do",
    "priority": "High",
    "assigned_to": 1,
    "project": 1,
    "created_at": "2024-12-16T12:00:00Z",
    "due_date": "2024-12-20T12:00:00Z"
  }
]
Create Task

POST /api/projects/{project_id}/tasks/
Body:
json
Copy code
{
  "title": "New Task",
  "description": "Description of the new task",
  "status": "To Do",
  "priority": "Medium",
  "assigned_to": 1,
  "project": 1,
  "due_date": "2024-12-20T12:00:00Z"
}
Retrieve Task

GET /api/tasks/{id}/
Response:
json
Copy code
{
  "id": 1,
  "title": "Task 1",
  "description": "Description of Task 1",
  "status": "To Do",
  "priority": "High",
  "assigned_to": 1,
  "project": 1,
  "created_at": "2024-12-16T12:00:00Z",
  "due_date": "2024-12-20T12:00:00Z"
}
Update Task

PUT /api/tasks/{id}/
Body:
json
Copy code
{
  "title": "Updated Task",
  "description": "Updated task description",
  "status": "In Progress",
  "priority": "High",
  "assigned_to": 1,
  "project": 1,
  "due_date": "2024-12-21T12:00:00Z"
}
Delete Task

DELETE /api/tasks/{id}/
Response:
json
Copy code
{
  "message": "Task deleted successfully"
}
Comments
List Comments

GET /api/tasks/{task_id}/comments/
Response:
json
Copy code
[
  {
    "id": 1,
    "content": "Comment on Task 1",
    "user": 1,
    "task": 1,
    "created_at": "2024-12-16T12:00:00Z"
  }
]
Create Comment

POST /api/tasks/{task_id}/comments/
Body:
json
Copy code
{
  "content": "This is a comment",
  "user": 1,
  "task": 1
}
Retrieve Comment

GET /api/comments/{id}/
Response:
json
Copy code
{
  "id": 1,
  "content": "Comment on Task 1",
  "user": 1,
  "task": 1,
  "created_at": "2024-12-16T12:00:00Z"
}
Update Comment

PUT /api/comments/{id}/
Body:
json
Copy code
{
  "content": "Updated comment content",
  "user": 1,
  "task": 1
}
Delete Comment

DELETE /api/comments/{id}/
Response:
json
Copy code
{
  "message": "Comment deleted successfully"
}
API Documentation (Swagger)
Once the server is running, visit the following URL to access the Swagger UI for API documentation:

bash
Copy code
http://127.0.0.1:8000/swagger/
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributors
Your Name - Project lead, developer.
go
Copy code

This `README.md` includes installation steps, API endpoint descriptions, and instructions for accessing the Swagger UI for your project. You can copy and paste this into your `README.md` file. Let me know if you need further adjustments!