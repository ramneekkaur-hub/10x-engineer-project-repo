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

# ================== Edge Case Tests ==================

def test_list_prompts_with_empty_query():
    response = client.get("/prompts?search=")
    assert response.status_code == 200  # Or appropriate status
    assert "prompts" in response.json()

def test_list_prompts_with_special_characters():
    response = client.get("/prompts?search=%40%23%24%25")
    assert response.status_code == 200  # Or appropriate status
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
