import pytest
from pydantic import ValidationError
from app.models import Prompt  # Use the actual Prompt model for testing

# ================== Model Validation Tests ==================

def test_prompt_validation_success():
    # Initialize model with valid data
    prompt_instance = Prompt(title="Valid Title", content="Valid Content")
    assert prompt_instance.title == "Valid Title"
    assert prompt_instance.content == "Valid Content"


def test_prompt_validation_error():
    # Test model validation error by providing invalid data
    with pytest.raises(ValidationError):
        Prompt(title="", content="")  # Title and content require at least 1 character

# ================== Default Values Tests ==================

def test_prompt_default_values():
    # Test a model's default values are set correctly
    prompt_instance = Prompt(title="Title", content="Content")
    assert prompt_instance.updated_at is not None  # Updated at should be set

# ================== Serialization Tests ==================

def test_prompt_serialization():
    # Test serialization to dictionary or JSON
    prompt_instance = Prompt(title="Title", content="Content")
    prompt_dict = prompt_instance.dict()
    assert prompt_dict["title"] == "Title"
    assert prompt_dict["content"] == "Content"  # Adjust to match your actual model fields and values
