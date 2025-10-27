import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> list[int]:
    return [1234567891234567]


@pytest.mark.parametrize("card, expected", [("1234567891234567", "1234 56** **** 4567")])
def test_mask_card_number(card, expected) -> list[int]:
    assert get_mask_card_number(card) == expected


def test_invalid_mask_card_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number=123456789)


@pytest.fixture
def card_account() -> list[int]:
    return [12345678912345671111]


@pytest.mark.parametrize("card_account, expected", [("12345678912345671111", "**1111")])
def test_mask_card_account(card_account, expected):
    assert get_mask_account(card_account) == expected


# def test_invalid_mask_card_account (card_account):
#     with pytest.raises(ValueError):
#         get_mask_account(card_account = 123456789)
