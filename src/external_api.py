import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def transaction_info(transaction: dict) -> float | str:
    """Функция принимающая на вход транзакцию и возвращающая сумму транзакции (amount) в рублях"""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        currency_rub = "RUB"

        if currency != "RUB":
            url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
                   f"{currency_rub}&from={currency}&amount={amount}")
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            status_code = response.status_code
            result = response.json()
            if status_code != 200:
                print(f"Ошибка запроса: Код {status_code}, Описание: {result}")
                return 0.0
            if status_code == 200:
                return amount
            else:
                return 0.0
        else:
            return amount
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return 0.0


print(transaction_info(
    {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967",
    },
))

print(
    transaction_info(
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
        }
    )
)

print(
    transaction_info(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    )
)