import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_transaction_descriptions(currency_test_list, expected, should_raise: bool):
    if should_raise:
        with pytest.raises(ValueError):
            list(transaction_descriptions(currency_test_list))
    else:
        assert list(transaction_descriptions(currency_test_list)) == expected


def test_card_num_generators(card_num):
    """Тестирование функции на корректность длины номера карт и состоят ли они из цифр"""
    assert len(card_num) == 16, "Номер карты некорректной длины"
    assert card_num.isdigit(), "Номер карты содержит нецифровые символы"


def test_filter_by_currency_no_transactions(currency_test_list):
    """Тестирование функции на корректность отбора операций по валюте"""
    generator = filter_by_currency(currency_test_list, "EUR")
    try:
        next(generator)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


"""Параметризация для генератора номеров карт"""


@pytest.mark.parametrize("start, stop, expected_numbers", [
    (
        1,
        3,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    ),
    (
        2,
        3,
        [
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    )
])
def test_card_number_generator(start, stop, expected_numbers):
    gen = card_number_generator(start, stop)
    generated_numbers = list(gen)
    assert generated_numbers == expected_numbers


def test_card_number_format():
    """Тестирование формата номера карты"""
    gen = card_number_generator(1, 1)
    card_number = next(gen)
    """Тестирование формата номера карты - 4 группы по 4 цифры"""
    parts = card_number.split()
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()


def test_transaction_descriptions(currency_test_list):
    """Тестирование для функции описаний транзакций"""
    descriptions = list(transaction_descriptions(currency_test_list))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert descriptions == expected_descriptions


"""Параметризация для теста фильтрации по валюте"""


@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),
    ("EUR", []),
    ("RUB", [873106923, 594226727])
])
def test_filter_by_currency(currency_test_list, currency_code, expected_ids):
    result = list(filter_by_currency(currency_test_list, currency_code))
    result_ids = [x["id"] for x in result]
    assert result_ids == expected_ids


