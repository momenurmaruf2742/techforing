###### # Project Management Application

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

git clone <https://github.com/momenurmaruf2742/techforing.git>\
```cd project-management```

### 2. Set up a virtual environment

```python -m venv env```\
```source env/bin/activate```  # On Windows use `env\Scripts\activate`

### 3. Install dependencies

```pip install -r requirements.txt```

### 4. Configure the database

Make sure to set up your database in settings.py (default SQLite or configure PostgreSQL/MySQL).
Run migrations to create the database tables:

```python manage.py migrate```

### 5. Create a superuser

If you want to access the Django admin panel, create a superuser:

```python manage.py createsuperuser```

After createsuperuser you have to login through the username and password to get access token in postmat or any other api testing tools

```
POST /api/users/login/
Body:
json

{
  "username": "yourusername",
  "password": "yourpassword"
}
Response:
json

{
  "access_token": "your_access_token"
}
```

now use this `Bearer <token>` in swagger ui authorizations field

### 6. Run the development server

```python manage.py runserver```

##### API Documentation (Swagger)

Once the server is running, visit the following URL to access the Swagger UI for API documentation:

<http://127.0.0.1:8000/swagger/>
#### Optinal API Documentation
##### API Documentation (Postman)

<https://documenter.getpostman.com/view/16358865/2sAYHzH3ov>

# API Endpoints

# Users

### Register User

`POST /api/users/register/`

###### Body

```
json

{
  "username": "user1",
  "email": "user1@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Login User

```
POST /api/users/login/
Body:
json

{
  "username": "user1",
  "password": "password123"
}
Response:
json

{
  "access_token": "your_access_token"
}
```

### Get User Details

```
GET /api/users/{id}/
Response:
json

{
  "id": 1,
  "username": "user1",
  "email": "user1@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Update User

```
PUT /api/users/{id}/
Body:
json

{
  "username": "updated_username",
  "email": "updated_email@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Delete User

```
DELETE /api/users/{id}/
Response:
json

{
  "message": "User deleted successfully"
}
```

# Projects

### List Projects

```
GET /api/projects/
Response:
json

[
  {
    "id": 1,
    "name": "Project 1",
    "description": "Description of Project 1",
    "owner": 1,
    "created_at": "2024-12-16T12:00:00Z"
  }
]
```

### Create Project

```
POST /api/projects/
Body:
json

{
  "name": "New Project",
  "description": "Description of new project",
  "owner": 1
}
```

### Retrieve Project

```
GET /api/projects/{id}/
Response:
json

{
  "id": 1,
  "name": "Project 1",
  "description": "Description of Project 1",
  "owner": 1,
  "created_at": "2024-12-16T12:00:00Z"
}
```

### Update Project

```
PUT /api/projects/{id}/
Body:
json

{
  "name": "Updated Project",
  "description": "Updated description",
  "owner": 1
}
```

### Delete Project

```
DELETE /api/projects/{id}/
Response:
json

{
  "message": "Project deleted successfully"
}
```

# Tasks

### List Tasks

```
GET /api/projects/{project_id}/tasks/
Response:
json

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
```

### Create Task

```
POST /api/projects/{project_id}/tasks/
Body:
json

{
  "title": "New Task",
  "description": "Description of the new task",
  "status": "To Do",
  "priority": "Medium",
  "assigned_to": 1,
  "project": 1,
  "due_date": "2024-12-20T12:00:00Z"
}
```

### Retrieve Task

```
GET /api/tasks/{id}/
Response:
json

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
```

### Update Task

```
PUT /api/tasks/{id}/
Body:
json

{
  "title": "Updated Task",
  "description": "Updated task description",
  "status": "In Progress",
  "priority": "High",
  "assigned_to": 1,
  "project": 1,
  "due_date": "2024-12-21T12:00:00Z"
}
```

### Delete Task

```
DELETE /api/tasks/{id}/
Response:
json

{
  "message": "Task deleted successfully"
}
```

# Comments

### List Comments

```
GET /api/tasks/{task_id}/comments/
Response:
json

[
  {
    "id": 1,
    "content": "Comment on Task 1",
    "user": 1,
    "task": 1,
    "created_at": "2024-12-16T12:00:00Z"
  }
]
```

### Create Comment

```
POST /api/tasks/{task_id}/comments/
Body:
json

{
  "content": "This is a comment",
  "user": 1,
  "task": 1
}
```

### Retrieve Comment

```
GET /api/comments/{id}/
Response:
json

{
  "id": 1,
  "content": "Comment on Task 1",
  "user": 1,
  "task": 1,
  "created_at": "2024-12-16T12:00:00Z"
}
```

### Update Comment

```
PUT /api/comments/{id}/
Body:
json

{
  "content": "Updated comment content",
  "user": 1,
  "task": 1
}
```

### Delete Comment

```
DELETE /api/comments/{id}/
Response:
json

{
  "message": "Comment deleted successfully"
}
```

License
This project is licensed under the MIT License - see the LICENSE file for details.

```

Contributors
Momenur Islam

This `README.md` includes installation steps, API endpoint descriptions, and instructions for accessing the Swagger UI for your project. You can copy and paste this into your `README.md` file. Let me know if you need further adjustments!
```
