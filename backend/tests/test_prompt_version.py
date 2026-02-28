import pytest
from app.utils import select_prompt_version  # Corrected import path given the package structure

# Assuming there is a PromptVersion class or function that we need to test
def test_select_prompt_version():
    # Setup
    # Create or retrieve a mock list of prompt versions
    available_versions = ["v1.0", "v1.1", "v1.2"]

    # Test selecting a version
    selected_version = select_prompt_version("v1.1", available_versions)  # This method is now imported and used

    # Expected behavior: should return details of the version "v1.1"
    expected_details = {
        "version": "v1.1",
        "details": "Details about version 1.1"
    }

    assert selected_version == expected_details, "The selected version details do not match the expected output."


def test_invalid_prompt_version_selection():
    # Setup
    available_versions = ["v1.0", "v1.1", "v1.2"]

    # Test selecting a non-existing version
    with pytest.raises(ValueError):
        select_prompt_version("v2.0", available_versions)  # Assuming this raises a ValueError for an invalid selection

