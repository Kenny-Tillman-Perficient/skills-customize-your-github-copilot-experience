# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage tasks in memory. Practice defining routes, validating request data with Pydantic, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Read Tasks from the API

#### Description
Complete the FastAPI app so clients can retrieve all tasks or look up one task by its ID.

#### Requirements
Completed program should:

- Start a FastAPI application using the provided starter code.
- Implement `GET /tasks` to return the task list.
- Implement `GET /tasks/{task_id}` to return the matching task.
- Return an HTTP 404 response when the requested task ID does not exist.
- Run locally with Uvicorn so the routes can be tested through the interactive API documentation.

### 🛠️ Create, Update, and Delete Tasks

#### Description
Add routes that let clients create a task, change an existing task, and remove a task.

#### Requirements
Completed program should:

- Use a Pydantic model to validate task data submitted by clients.
- Implement `POST /tasks` to create a task with a unique ID and return HTTP 201.
- Implement `PUT /tasks/{task_id}` to update an existing task.
- Implement `DELETE /tasks/{task_id}` to remove an existing task.
- Return HTTP 404 when an update or delete request targets an ID that does not exist.