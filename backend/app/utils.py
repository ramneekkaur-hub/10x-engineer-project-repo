"""Utility functions for PromptLab"""

from typing import List
from app.models import Prompt


def sort_prompts_by_date(prompts: List[Prompt], descending: bool = True) -> List[Prompt]:
    """Sort prompts by creation date.
    
    Args:
        prompts: List of Prompt objects to sort.
        descending: If True, sort newest first. If False, sort oldest first.
            Defaults to True.
    
    Returns:
        A new list of prompts sorted by creation date.
    
    Example:
        >>> prompts = [prompt1, prompt2, prompt3]
        >>> sorted_prompts = sort_prompts_by_date(prompts, descending=True)
        >>> sorted_prompts[0].created_at >= sorted_prompts[1].created_at
        True
    """
    return sorted(prompts, key=lambda p: p.created_at, reverse=descending)


def filter_prompts_by_collection(prompts: List[Prompt], collection_id: str) -> List[Prompt]:
    """Filter prompts by collection ID.
    
    Args:
        prompts: List of Prompt objects to filter.
        collection_id: The collection ID to filter by.
    
    Returns:
        A new list containing only prompts that belong to the specified collection.
    
    Example:
        >>> prompts = [prompt1, prompt2, prompt3]
        >>> collection_prompts = filter_prompts_by_collection(prompts, "col_123")
        >>> len(collection_prompts) <= len(prompts)
        True
    """
    return [p for p in prompts if p.collection_id == collection_id]


def search_prompts(prompts: List[Prompt], query: str) -> List[Prompt]:
    """Search prompts by title or description.
    
    Args:
        prompts: List of Prompt objects to search.
        query: Search query string (case-insensitive).
    
    Returns:
        A new list of prompts matching the search query in title or description.
    
    Example:
        >>> prompts = [prompt1, prompt2, prompt3]
        >>> results = search_prompts(prompts, "python")
        >>> all("python" in p.title.lower() or "python" in p.description.lower() 
        ...     for p in results)
        True
    """
    query_lower = query.lower()
    return [
        p for p in prompts 
        if query_lower in p.title.lower() or 
           (p.description and query_lower in p.description.lower())
    ]


def validate_prompt_content(content: str) -> bool:
    """Validate prompt content meets minimum requirements.
    
    A valid prompt must:
    - Not be empty or whitespace-only
    - Be at least 10 characters long
    
    Args:
        content: The prompt content string to validate.
    
    Returns:
        True if content is valid, False otherwise.
    
    Example:
        >>> validate_prompt_content("Hello world!")
        True
        >>> validate_prompt_content("short")
        False
    """
    if not content or not content.strip():
        return False
    return len(content.strip()) >= 10


def extract_variables(content: str) -> List[str]:
    """Extract template variables from prompt content.
    
    Variables are identified by the format {{variable_name}} where variable_name
    contains only word characters (letters, digits, underscore).
    
    Args:
        content: The prompt content to extract variables from.
    
    Returns:
        A list of variable names found in the content (duplicates included).
    
    Example:
        >>> content = "Hello {{name}}, your score is {{score}}"
        >>> extract_variables(content)
        ['name', 'score']
    """
    import re
    pattern = r'\{\{(\w+)\}\}'
    return re.findall(pattern, content)
