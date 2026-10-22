from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TaskInput(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read the API docs", "description": "Explore the available routes", "completed": False},
    {"id": 2, "title": "Build a route", "description": "Add a FastAPI endpoint", "completed": True},
]


@app.get("/tasks")
def list_tasks():
    # Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Return the task with this ID, or an HTTP 404 response.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskInput):
    # Assign a unique ID, add the task, and return it.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskInput):
    # Replace the matching task, or return an HTTP 404 response.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Remove the matching task, or return an HTTP 404 response.
    pass