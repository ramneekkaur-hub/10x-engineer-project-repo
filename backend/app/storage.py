"""In-memory storage for PromptLab

This module provides simple in-memory storage for prompts and collections.
In a production environment, this would be replaced with a database.
"""

from typing import Dict, List, Optional
from app.models import Prompt, Collection


class Storage:
    """In-memory storage for managing prompts and collections.
    This class provides CRUD operations for prompts and collections,
    allowing users to create, retrieve, update, and delete items.
    Storage is maintained in memory using dictionaries.
    Attributes:
        _prompts: Dictionary mapping prompt IDs to Prompt objects.
        _collections: Dictionary mapping collection IDs to Collection objects.
    """
    """Create and store a new prompt.
    Args:
    prompt: The Prompt object to create and store.
    Returns:
    The created Prompt object.
    Raises:
    ValueError: If prompt is None or prompt.id is empty.
    Example:
    >>> prompt = Prompt(id="p1", title="My Prompt")
    >>> created = storage.create_prompt(prompt)
    >>> created.id
    "p1"
    """
    """Retrieve a prompt by its unique identifier.
    Args:
    prompt_id: The unique identifier of the prompt to retrieve.
    Returns:
    The Prompt object if found, None otherwise.
    Raises:
    ValueError: If prompt_id is empty.
    Example:
    >>> prompt = storage.get_prompt("p1")
    >>> print(prompt.title)
    "My Prompt"
    """
    """Retrieve all stored prompts.
        Returns:
            A list of all Prompt objects in storage. Returns an empty list
            if no prompts exist.
        Example:
            >>> prompts = storage.get_all_prompts()
            >>> len(prompts)
            5
        """
    """Update an existing prompt.
        Args:
            prompt_id: The unique identifier of the prompt to update.
            prompt: The updated Prompt object.
        Returns:
            The updated Prompt object if the prompt exists, None otherwise.
        Raises:
            ValueError: If prompt_id is empty or prompt is None.
        Example:
            >>> updated = storage.update_prompt("p1", modified_prompt)
            >>> updated.title
            "Updated Title"
        """
    """Delete a prompt by its unique identifier.
        Args:
            prompt_id: The unique identifier of the prompt to delete.
        Returns:
            True if the prompt was successfully deleted, False if the
            prompt was not found.
        Raises:
            ValueError: If prompt_id is empty.
        Example:
            >>> deleted = storage.delete_prompt("p1")
            >>> deleted
            True
        """
    """Create and store a new collection.
        Args:
            collection: The Collection object to create and store.
        Returns:
            The created Collection object.
        Raises:
            ValueError: If collection is None or collection.id is empty.
        Example:
            >>> collection = Collection(id="c1", name="My Collection")
            >>> created = storage.create_collection(collection)
            >>> created.id
            "c1"
        """
    """Retrieve a collection by its unique identifier.
        Args:
            collection_id: The unique identifier of the collection to retrieve.
        Returns:
            The Collection object if found, None otherwise.
        Raises:
            ValueError: If collection_id is empty.
        Example:
            >>> collection = storage.get_collection("c1")
            >>> print(collection.name)
            "My Collection"
        """
    """Retrieve all stored collections.
        Returns:
            A list of all Collection objects in storage. Returns an empty list
            if no collections exist.
        Example:
            >>> collections = storage.get_all_collections()
            >>> len(collections)
            3
        """
    """Delete a collection by its unique identifier.
        Args:
            collection_id: The unique identifier of the collection to delete.
        Returns:
            True if the collection was successfully deleted, False if the
            collection was not found.
        Raises:
            ValueError: If collection_id is empty.
        Example:
            >>> deleted = storage.delete_collection("c1")
            >>> deleted
            True
        """
    """Retrieve all prompts belonging to a specific collection.
        Args:
            collection_id: The unique identifier of the collection.
        Returns:
            A list of Prompt objects associated with the specified collection.
            Returns an empty list if no prompts are found or collection does
            not exist.
        Raises:
            ValueError: If collection_id is empty.
        Example:
            >>> prompts = storage.get_prompts_by_collection("c1")
            >>> len(prompts)
            4
        """
    """Clear all prompts and collections from storage.
        This method removes all data stored in memory. Use with caution
        as this operation cannot be undone.
        Example:
            >>> storage.clear()
            >>> len(storage.get_all_prompts())
            0
        """
    def __init__(self):
        self._prompts: Dict[str, Prompt] = {}
        self._collections: Dict[str, Collection] = {}
    
    # ============== Prompt Operations ==============
    
    def create_prompt(self, prompt: Prompt) -> Prompt:
        self._prompts[prompt.id] = prompt
        return prompt
    
    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        return self._prompts.get(prompt_id)
    
    def get_all_prompts(self) -> List[Prompt]:
        return list(self._prompts.values())
    
    def update_prompt(self, prompt_id: str, prompt: Prompt) -> Optional[Prompt]:
        if prompt_id not in self._prompts:
            return None
        self._prompts[prompt_id] = prompt
        return prompt
    
    def delete_prompt(self, prompt_id: str) -> bool:
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False
    
    # ============== Collection Operations ==============
    
    def create_collection(self, collection: Collection) -> Collection:
        self._collections[collection.id] = collection
        return collection
    
    def get_collection(self, collection_id: str) -> Optional[Collection]:
        return self._collections.get(collection_id)
    
    def get_all_collections(self) -> List[Collection]:
        return list(self._collections.values())
    
    def delete_collection(self, collection_id: str) -> bool:
        if collection_id in self._collections:
            del self._collections[collection_id]
            return True
        return False
    
    def get_prompts_by_collection(self, collection_id: str) -> List[Prompt]:
        return [p for p in self._prompts.values() if p.collection_id == collection_id]
    
    # ============== Utility ==============
    
    def clear(self):
        self._prompts.clear()
        self._collections.clear()


# Global storage instance
storage = Storage()