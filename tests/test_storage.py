import pytest
from app.storage import Storage
from app.models import Prompt, Collection

@pytest.fixture
def storage():
    return Storage()

# ================== Prompt CRUD Tests ==================

def test_create_and_get_prompt(storage):
    prompt = Prompt(id="p1", title="Test Prompt", content="Sample content")
    storage.create_prompt(prompt)
    retrieved = storage.get_prompt(prompt.id)
    assert retrieved is not None
    assert retrieved.id == prompt.id
    assert retrieved.title == prompt.title

def test_update_prompt(storage):
    prompt = Prompt(id="p2", title="Old Title", content="Old Content")
    storage.create_prompt(prompt)
    updated_prompt = Prompt(id="p2", title="New Title", content="New Content")
    storage.update_prompt(prompt.id, updated_prompt)
    updated = storage.get_prompt(prompt.id)
    assert updated.title == "New Title"
    assert updated.content == "New Content"

def test_delete_prompt(storage):
    prompt = Prompt(id="p3", title="To be deleted", content="Content")
    storage.create_prompt(prompt)
    success = storage.delete_prompt(prompt.id)
    assert success is True
    assert storage.get_prompt(prompt.id) is None

# ================== Collection CRUD Tests ==================

def test_create_and_get_collection(storage):
    collection = Collection(id="c1", name="Test Collection")
    storage.create_collection(collection)
    retrieved = storage.get_collection(collection.id)
    assert retrieved is not None
    assert retrieved.id == collection.id
    assert retrieved.name == collection.name

def test_delete_collection(storage):
    collection = Collection(id="c2", name="Delete Test")
    storage.create_collection(collection)
    success = storage.delete_collection(collection.id)
    assert success is True
    assert storage.get_collection(collection.id) is None

# ================== Data Persistence Tests ==================

def test_data_persistence_within_session(storage):
    prompt = Prompt(id="p4", title="Persist Test", content="Content")
    storage.create_prompt(prompt)
    collection = Collection(id="c3", name="Persist Collection")
    storage.create_collection(collection)
    # Ensure data is persisted within the session
    assert len(storage.get_all_prompts()) == 1
    assert len(storage.get_all_collections()) == 1

def test_clear_storage(storage):
    prompt = Prompt(id="p5", title="Persist Test", content="Content")
    storage.create_prompt(prompt)
    collection = Collection(id="c4", name="Persist Collection")
    storage.create_collection(collection)
    storage.clear()
    assert len(storage.get_all_prompts()) == 0
    assert len(storage.get_all_collections()) == 0

# ================== Edge Case Tests ==================

def test_get_nonexistent_prompt(storage):
    assert storage.get_prompt("nonexistent") is None

def test_get_nonexistent_collection(storage):
    assert storage.get_collection("nonexistent") is None
