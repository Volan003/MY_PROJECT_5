import json


def get_transactions_list(path: str) -> list[dict]:
    """Получение списка словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as transactions_list:
            try:
                transactions_list = json.load(transactions_list)
            except json.decoder.JSONDecodeError:
                print('Файл не содержит список или не найден')
                return []
            return transactions_list
    except FileNotFoundError:
        print('Файл не найден')
        return []


if __name__ == "__main__":
    get_transactions_list('C:/Users/volod/PycharmProjects/MY_PROJECT_5/data/operations.json')
