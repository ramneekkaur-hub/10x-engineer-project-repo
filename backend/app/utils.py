from datetime import datetime
from typing import List, Dict, Any


def sort_prompts_by_date(prompts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sort prompts by date.
    Args:
        prompts (list): List of prompt data, each having a date field.
    Returns:
        list: Sorted list of prompts by date.
    Raises:
        ValueError: If any date is not in a valid format.
    """
    def parse_date(prompt: Dict[str, Any]) -> datetime:
        date_str = prompt.get('date', '')
        try:
            return datetime.fromisoformat(date_str)
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}") from e

    return sorted(prompts, key=parse_date)
def select_prompt_version(version: str, available_versions: List[str]) -> Dict[str, str]:
    """
    Select a specific prompt version from available versions.
    Args:
        version (str): The version to select.
        available_versions (list): List of available version strings.

    Returns:
        dict: Details of the selected version.

    Raises:
        ValueError: If the version is not available.
    """
    if version not in available_versions:
        raise ValueError(f"Version {version} not found in available versions.")

    return {
        "version": version,
        "details": f"Details about version {version[1:]}"
    }


def filter_prompts_by_collection(prompts: List[Dict[str, Any]], collection: str) -> List[Dict[str, Any]]:
    """
    Filter prompts by specific collection.
    Args:
        prompts (list): List of prompt data.
        collection (str): The collection to filter by.
    Returns:
        list: Prompts belonging to the specified collection.
    """
    return [prompt for prompt in prompts if prompt.get('collection') == collection]


def search_prompts(prompts: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
    """
    Search prompts matching the search term.

    Args:
        prompts (list): List of prompt data.
        search_term (str): The term to search for within the prompts.

    Returns:
        list: Prompts that include the search term.
    """
    return [prompt for prompt in prompts if search_term.lower() in prompt.get('text', '').lower()]

