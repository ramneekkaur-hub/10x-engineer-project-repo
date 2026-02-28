import pytest
from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

# ================== Happy Path Tests ==================

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_list_prompts():
    response = client.get("/prompts")
    assert response.status_code == 200
    assert "prompts" in response.json()

# New tests for successful collection operations

def test_create_collection():
    response = client.post("/collections", json={
        "name": "Sample Collection",
        "description": "Description here"
    })
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["name"] == "Sample Collection"


def test_list_collections():
    response = client.get("/collections")
    assert response.status_code == 200
    assert "collections" in response.json()

# ================== Error Case Tests ==================


def test_get_prompt_not_found():
    response = client.get("/prompts/nonexistent_id")
    assert response.status_code == 404


def test_create_prompt_invalid_collection():
    response = client.post("/prompts", json={
        "title": "Sample",
        "content": "Sample content",
        "collection_id": "nonexistent_collection"
    })
    assert response.status_code == 400


def test_delete_collection_removes_prompts():
    # Create a collection
    collection_response = client.post("/collections", json={
        "name": "Temp Collection",
        "description": "Temporary for testing"
    })
    assert collection_response.status_code == 201
    collection_id = collection_response.json()["id"]

    # Create a prompt linked to the collection
    prompt_response = client.post("/prompts", json={
        "title": "Prompt in Collection",
        "content": "Content here",
        "collection_id": collection_id
    })
    assert prompt_response.status_code == 201

    # Delete the collection
    delete_response = client.delete(f"/collections/{collection_id}")
    assert delete_response.status_code == 204

    # Ensure prompt no longer exists
    prompt_id = prompt_response.json()["id"]
    fetch_prompt_response = client.get(f"/prompts/{prompt_id}")
    assert fetch_prompt_response.status_code == 404

# ================== Edge Case Tests ==================


def test_list_prompts_with_empty_query():
    response = client.get("/prompts?search=")
    assert response.status_code == 200
    assert "prompts" in response.json()


def test_list_prompts_with_special_characters():
    response = client.get("/prompts?search=%40%23%24%25")
    assert response.status_code == 200
    assert "prompts" in response.json()

# ================== Query Parameter Tests ==================


def test_list_prompts_with_sorting():
    response = client.get("/prompts?sort_by=date")
    assert response.status_code == 200
    assert "prompts" in response.json()


def test_list_prompts_filtering_by_collection():
    response = client.get("/prompts?collection_id=valid_collection_id")
    assert response.status_code == 200
    assert "prompts" in response.json()
