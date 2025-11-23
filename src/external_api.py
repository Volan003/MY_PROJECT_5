import os
import requests
from src.utils import get_transactions_list

from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


def transaction_info (transaction_list):
    """Функция принимающая на вход транзакцию и возвращающая сумму транзакции (amount) в рублях"""
    for i in transaction_list:
        if i["operationAmount"]["currency"]["code"] == "RUB":
            return i["operationAmount"]["amount"]
        if i["operationAmount"]["currency"]["code"] != 'RUB':
            response = requests.get (f"https://api.apilayer.com/exchangerates_data/convert?to={i["operationAmount"]["currency"]["code"]}&from={i["operationAmount"]["currency"]["code"]}&amount={i["operationAmount"]["amount"]}-{API_KEY}")
            return response.json()


if __name__ == "__main__":
    transaction_info (get_transactions_list())