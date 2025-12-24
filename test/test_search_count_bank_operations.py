import pytest

from src.search_count_bank_operations import process_bank_search, process_bank_operations


@pytest.fixture()
def operations():
    result = [{"description": "Перевод организации"},
            {"description": "Открытие вклада"},
            {"description": "Перевод организации"}]
    return result


def test_process_bank_search(operations):
    result = process_bank_search(operations, "открытие")
    expected = [{"description": "Открытие вклада"}]
    assert result == expected

def test_process_bank_operations(operations):
    assert process_bank_operations(operations, ["Перевод организации"]) == {"Перевод организации": 2}