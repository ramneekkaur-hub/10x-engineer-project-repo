from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import uuid4

def generate_id() -> str:
    """Generate a new unique identifier using UUID4.

    Returns:
        A string representation of a new unique identifier.
    """
    return str(uuid4())


def get_current_time() -> datetime:
    """Get the current UTC time.

    Returns:
        The current datetime in UTC.
    """
    return datetime.utcnow()

# ============== Prompt Models ==============

class PromptBase(BaseModel):
    """Represents the core structure of a prompt including title and content.

    Attributes:
        title: The title of the prompt.
        content: The actual content of the prompt.
        description: An optional description providing more context.
        collection_id: An optional identifier for the prompt's collection.
    """
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=500)
    collection_id: Optional[str] = None


class PromptCreate(PromptBase):
    """Pydantic model for creating a new prompt, inheriting from PromptBase."""
    pass


class PromptUpdate(PromptBase):
    """Pydantic model for updating an existing prompt, inheriting from PromptBase."""
    pass


class Prompt(PromptBase):
    """Pydantic model for a full prompt with ID and timestamps.

    Attributes:
        id: A unique identifier for the prompt.
        created_at: The datetime when the prompt was created.
        updated_at: The datetime when the prompt was last updated.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)

    class Config:
        from_attributes = True


# ============== Collection Models ==============

class CollectionBase(BaseModel):
    """Represents the core structure of a collection including name and description.

    Attributes:
        name: The name of the collection.
        description: An optional description of the collection.
    """
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class CollectionCreate(CollectionBase):
    """Pydantic model for creating a new collection, inheriting from CollectionBase."""
    pass


class Collection(CollectionBase):
    """Pydantic model for a full collection with ID and timestamps.

    Attributes:
        id: A unique identifier for the collection.
        created_at: The datetime when the collection was created.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)

    class Config:
        from_attributes = True


# ============== Response Models ==============

class PromptList(BaseModel):
    """Model for a list of prompts with a total count.

    Attributes:
        prompts: A list of Prompt objects.
        total: The total number of prompts.
    """
    prompts: List[Prompt]
    total: int


class CollectionList(BaseModel):
    """Model for a list of collections with a total count.

    Attributes:
        collections: A list of Collection objects.
        total: The total number of collections.
    """
    collections: List[Collection]
    total: int


class HealthResponse(BaseModel):
    """Model for representing an API health check response.

    Attributes:
        status: The status of the API health check.
        version: The version of the current API.
    """
    status: str
    version: str
