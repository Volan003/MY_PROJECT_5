import json
import os
from unittest.mock import patch
from src.external_api import transaction_info, API_KEY
from src.utils import get_transactions_list

transaction_usd =\
    {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
    }

amount = float(transaction_usd["operationAmount"]["amount"])
currency = transaction_usd["operationAmount"]["currency"]["code"]
currency_rub = "RUB"


@patch('requests.get')
def test_transaction_info(mock_get):
    mock_get.return_value.json.return_value = {"result": 0.0}
    result = transaction_info(transaction_usd)
    assert result == 0.0
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to={currency_rub}&from={currency}&amount={amount}",
        headers={"apikey": API_KEY}
    )


def load_operations(path: str) -> list[dict] | dict:
    """Чтение файла"""
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []
    else:
        with open(path, encoding='utf-8') as f:
            open_file = json.load(f)
            if not isinstance(open_file, list):
                return []
            return open_file


@patch('os.path.getsize')
@patch('os.path.exists')
def test_file_not_empty(mock_getsize, mock_exists=None):
    mock_getsize.return_value = 0
    mock_exists.return_value = True
    assert load_operations('empty_file_json') == []
    mock_getsize.assert_called_with('empty_file_json')