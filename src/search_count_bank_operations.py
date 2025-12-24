import re
from collections import Counter
from src.read_csv_excel_files import read_csv_func, read_excel_func
from src.utils import get_transactions_list

data = read_excel_func("../data/transactions_excel.xlsx")
# data = read_csv_func("../data/transactions.csv")
# data = get_transactions_list("../data/operations.json")

def process_bank_search(data:list[dict], keyword:str)->list[dict]:
    """Функция, которая будет принимать список словарей с данными
    о банковских операциях и строку поиска, а возвращать список словарей,
    у которых в описании есть данная строка"""
    word_in_description = []
    for operation in data:
        description = operation.get('description', '')
        if isinstance(description, str) and re.search(keyword, description, re.IGNORECASE):
            word_in_description.append(operation)
    return word_in_description

if __name__ == "__main__":
    print(process_bank_search(data,"Перевод"))

def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории.
    """
    category_counts = Counter(
        operation.get('description') for operation in data if operation.get('description') in categories
    )
    return dict(category_counts)

if __name__ == "__main__":
    filtered_data = process_bank_search(data, "Перевод")
    categories = ['Перевод на счёт', 'Перевод на карту']
    category_counts = process_bank_operations(filtered_data, categories)
    print(category_counts)
    print(f'Количество операций: {len(filtered_data)}')
    print(f'Количество операций: {Counter(categories)}')