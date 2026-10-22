import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(
        main,
        "tasks",
        [
            {
                "id": 1,
                "title": "Read the API docs",
                "description": "Explore the available routes",
                "completed": False,
            },
            {
                "id": 2,
                "title": "Build a route",
                "description": "Add a FastAPI endpoint",
                "completed": True,
            },
        ],
    )
    return TestClient(main.app)


# TODO: Write tests for listing and retrieving tasks.
# TODO: Test the 404 response for a task ID that does not exist.
# TODO: Test creating, updating, and deleting tasks.