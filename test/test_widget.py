import sys
import os
# Добавь путь к корню проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def account_card():
    return "Platinum 1596837868705191"

def test_account_card(account_card):
    assert mask_account_card(account_card) == "Platinum 1596 83** **** 5191"

@pytest.fixture
def date_time ():
    return "2024-03-11T02:26:18.671407"

def test_date_time(date_time):
    assert get_date (date_time) == "11.03.2024"