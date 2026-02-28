import pytest

from app.utils import sort_prompts_by_date, filter_prompts_by_collection  # Import utility functions here

# ================== Utility Function Tests ==================






def test_sort_prompts_by_date():
    prompts = [{'date': '2021-01-01'}, {'date': '2020-01-01'}]
    sorted_prompts = sort_prompts_by_date(prompts)
    assert sorted_prompts == [{'date': '2020-01-01'}, {'date': '2021-01-01'}]

def test_filter_prompts_by_collection():
    prompts = [{'collection': '1'}, {'collection': '2'}]
    filtered_prompts = filter_prompts_by_collection(prompts, '1')
    assert filtered_prompts == [{'collection': '1'}]
# ================== Edge Case Tests ==================










# Replace with specific edge case tests for new utility functions if applicable
def test_sort_prompts_by_date_empty_list():
    sorted_prompts = sort_prompts_by_date([])
    assert sorted_prompts == []

def test_filter_prompts_by_collection_no_matching():
    prompts = [{'collection': '1'}, {'collection': '2'}]
    filtered_prompts = filter_prompts_by_collection(prompts, '3')
    assert filtered_prompts == []
# ================== Error Condition Tests ==================

# Replace with specific error condition tests for new utility functions if applicable
def test_sort_prompts_by_date_invalid_format():
    with pytest.raises(ValueError):  # Assuming your function raises ValueError for invalid format
        sort_prompts_by_date([{'date': 'invalid-date'}])

def test_filter_prompts_by_collection_invalid_type():
    with pytest.raises(TypeError):  # Assuming your function raises TypeError for invalid input type
        filter_prompts_by_collection(123, '1')
