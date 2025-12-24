import os
import re

from src.read_csv_excel_files import read_csv_func, read_excel_func
from src.utils import get_transactions_list

json_path = os.path.join(os.getcwd(), 'data', 'operations.json')
csv_path = os.path.join(os.getcwd(), 'data', 'transactions.csv')
xlsx_path = os.path.join(os.getcwd(), 'data', 'transactions_excel.xlsx')


def main():
    """Главная функция для работы приложения, которая отвечает за основную логику
    и связывает функциональность между собой"""
    # Первый цикл - выбор формата файла
    while True:
        user_choice = input('Выберите необходимый пункт меню:\n '
                            '1. Получить информацию о транзакциях из JSON-файла\n '
                            '2. Получить информацию о транзакциях из CSV-файла\n '
                            '3. Получить информацию о транзакциях из XLSX-файла\n Ответ: ')
        if user_choice == '1':
            data = get_transactions_list(json_path)
            print('Для обработки выбран JSON-файл.')
            break
        elif user_choice == '2':
            data = read_csv_func(csv_path)
            print('Для обработки выбран CSV-файл.')
            break
        elif user_choice == '3':
            data = read_excel_func(xlsx_path)
            print('Для обработки выбран XLSX-файл.')
            break
        else:
            print('Ошибка! Вы ввели несуществующий пункт меню.')
            continue

# Второй цикл - фильтр статуса операции
    while True:
        user_choice_1 = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                              'Доступные для фильтровки статусы: '
                              'EXECUTED, CANCELED, PENDING\nОтвет: ').upper()
        if user_choice_1 == 'EXECUTED' or user_choice_1 == 'CANCELED' or user_choice_1 == 'PENDING':
            print(f'Операции отфильтрованы по статусу {user_choice_1}')
            result = list(filter(lambda x: isinstance(x, dict) and x.get("state") == user_choice_1, data))
            break
        else:
            print(f'Статус операции {user_choice_1} недоступен.')
            continue

# Третий цикл для сортировки по дате
    while True:
        user_choice_2 = input('Отсортировать операции по дате? Да/Нет\nОтвет: ').lower()
        if user_choice_2 == 'да':
            result_2 = list(sorted(result, key=lambda x: x["date"]))  # используем "result" из предыдущего цикла
            break
        elif user_choice_2 == 'нет':
            result_2 = result
            break
        else:
            print(f'Фильтр {user_choice_2} недоступен.')
            continue

# Четвертый цикл для сортировки по возрастанию или убыванию
    while True:
        user_choice_3 = input('Отсортировать по возрастанию или по убыванию?\nОтвет: ').lower()
        if user_choice_3 == 'по возрастанию':
            result_3 = list(sorted(result_2, key=lambda x: x["id"]))  # используем "result" из предыдущего цикла
            break
        elif user_choice_3 == 'по убыванию':
            # используем "result" из предыдущего цикла
            result_3 = list(sorted(result_2, key=lambda x: x["id"], reverse=True))
            break
        else:
            print(f'Фильтр {user_choice_3} недоступен.')
            continue

# Пятый цикл для сортировки по валюте
    while True:
        user_choice_4 = input('Выводить только рублевые транзакции? Да/Нет\nОтвет: ').lower()
        if user_choice_4 == 'да':
            result_4 = [x for x in result_3 if x.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']
            break
        elif user_choice_4 == 'нет':
            result_4 = result_3
            break
        else:
            print(f'Фильтр {user_choice_4} недоступен.')
            continue

# Шестой цикл для сортировки по ключевым словам
    successful_filter = False
    while not successful_filter:
        user_choice_5 = input('Отфильтровать список транзакций по определенному слову в описании? '
                              'Да/Нет\n'
                              'Ответ: ').lower()
        if user_choice_5 == 'да':
            while True:
                word_in_description = input('Введите слово: ')
                # используем "result" из предыдущего цикла
                result_5 = list(filter(lambda x: re.search(word_in_description, x['description']), result_4))
                if result_5:
                    print("Найденные транзакции:", result_5)
                    successful_filter = True
                    break
                else:
                    print('Такого слова нет, попробуйте снова.')
        elif user_choice_5 == 'нет':
            result_5 = result_4
            successful_filter = True
        else:
            print(f'Фильтр {user_choice_5} недоступен.')
            continue
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(result_5)}')
    print(result_5)
    if not result_5:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == '__main__':
    main()
