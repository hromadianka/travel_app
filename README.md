# Travel Project Manager API

## Overview

Travel Project Manager is a REST API built with Django and Django REST Framework that allows users to create and manage travel projects, collect places they want to visit, add notes, and track visited locations.

The application integrates with the Art Institute of Chicago API to validate and import places using external artwork IDs.

## Features

### Authentication

* JWT authentication using SimpleJWT
* Protected API endpoints
* Access and refresh tokens

### Travel Projects

* Create travel projects
* Update travel projects
* Delete travel projects
* List all travel projects
* Retrieve a single travel project

### Places

* Add places to a project
* Create a project with places in a single request
* Update place notes
* Mark places as visited
* List all places in a project
* Retrieve a single place

### Business Rules

* A project may contain a maximum of 10 places
* Duplicate places are not allowed within the same project
* Places must exist in the Art Institute of Chicago API before being added
* A project cannot be deleted if any of its places have been marked as visited
* A project is automatically marked as completed when all places are visited

---

## Technology Stack

* Python 3.13
* Django
* Django REST Framework
* SQLite
* SimpleJWT
* Requests

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd travel_app
```

### Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

## Environment Variables

No environment variables are required for local development.

The application uses SQLite by default.

---

## Authentication

### Obtain JWT Token

**POST**

```text
/api/token/
```

Request body:

```json
{
  "username": "admin",
  "password": "your_password"
}
```

Response:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

### Refresh Token

**POST**

```text
/api/token/refresh/
```

Request body:

```json
{
  "refresh": "<refresh_token>"
}
```

### Authorized Requests

Include the access token in the Authorization header:

```http
Authorization: Bearer <access_token>
```

---

## API Documentation

Swagger/OpenAPI documentation is available at:

```text
/api/docs/
```

OpenAPI schema:

```text
/api/schema/
```

---

## API Endpoints

### Projects

#### List Projects

```http
GET /api/projects/
```

#### Retrieve Project

```http
GET /api/projects/{project_id}/
```

#### Create Project

```http
POST /api/projects/
```

Example:

```json
{
  "name": "Trip to Chicago",
  "description": "Museum tour",
  "start_date": "2026-06-10"
}
```

#### Create Project with Places

```http
POST /api/projects/
```

Example:

```json
{
  "name": "Chicago Art Tour",
  "description": "Art Institute visit",
  "places": [129884, 111222]
}
```

#### Update Project

```http
PATCH /api/projects/{project_id}/
```

Example:

```json
{
  "name": "Updated Project Name"
}
```

#### Delete Project

```http
DELETE /api/projects/{project_id}/
```

---

### Places

#### Add Place to Project

```http
POST /api/projects/{project_id}/places/
```

Example:

```json
{
  "external_id": 129884
}
```

#### List Places in Project

```http
GET /api/projects/{project_id}/places/
```

#### Retrieve Place

```http
GET /api/projects/{project_id}/places/{place_id}/
```

#### Update Place

```http
PATCH /api/projects/{project_id}/places/{place_id}/
```

Example:

```json
{
  "notes": "Must visit during the morning.",
  "visited": true
}
```

---

## Example Workflow

### 1. Obtain JWT Token

```http
POST /api/token/
```

### 2. Create a Project

```http
POST /api/projects/
```

### 3. Add Places

```http
POST /api/projects/{project_id}/places/
```

### 4. Update Places

```http
PATCH /api/projects/{project_id}/places/{place_id}/
```

### 5. Mark All Places as Visited

When all places in a project are marked as visited, the project status is automatically updated to:

```json
{
  "status": "completed"
}
```

---

## External API

This project uses the Art Institute of Chicago API for place validation.

Documentation:

https://api.artic.edu/docs/

Example endpoint:

```text
https://api.artic.edu/api/v1/artworks/{external_id}
```

