# 📘 Assignment: Testing FastAPI Endpoints with pytest

## 🎯 Objective

Write automated tests for a FastAPI task API using pytest and FastAPI's test client. Verify that endpoints return the expected data and status codes without starting a web server.

## 📝 Tasks

### 🛠️ Test API Read Endpoints

#### Description
Use the provided test scaffold to check that clients can list tasks and retrieve a task by ID.

#### Requirements
Completed program should:

- Save the completed API from the FastAPI assignment in a file named `main.py` in the same folder as the tests.
- Install the test dependencies with `pip install pytest httpx`.
- Use `TestClient` to send requests to the API without launching Uvicorn.
- Test that `GET /tasks` returns HTTP 200 and the expected tasks.
- Test that `GET /tasks/{task_id}` returns HTTP 200 and the matching task.
- Run the tests with `pytest -v`.

### 🛠️ Test Errors and Task Changes

#### Description
Add tests for missing task IDs and for creating, updating, and deleting tasks. Keep tests independent so each starts with the same sample data.

#### Requirements
Completed program should:

- Test that requesting a task ID that does not exist returns HTTP 404.
- Test that `POST /tasks` creates a task, returns HTTP 201, and includes the submitted task data in its response.
- Test that `PUT /tasks/{task_id}` updates an existing task and returns the updated data.
- Test that `DELETE /tasks/{task_id}` removes the task; accept HTTP 200 or 204, then verify that retrieving the deleted task returns HTTP 404.
- Use the provided pytest fixture to reset the sample tasks before each test.