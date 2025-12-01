import json
import logging
import os

logger = logging.getLogger('utils')
os.makedirs('logs', exist_ok=True)
file_handler = logging.FileHandler('logs/utils.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_list(path: str) -> list[dict]:
    """Получение списка словарей с данными о финансовых транзакциях"""
    logger.info('Начало работы программы - Получение списка словарей')
    try:
        with open(path, encoding="utf-8") as transactions_list:
            try:
                transactions_list = json.load(transactions_list)
            except json.decoder.JSONDecodeError:
                logger.error(f'Файл {path} не содержит список или не найден')
                print('Файл не содержит список или не найден')
                return []
            logger.info('Окончание работы программы - Вывод списка словарей')
            return transactions_list
    except FileNotFoundError:
        logger.error('Ошибка - FileNotFoundError')
        print('Файл не найден')
        return []


if __name__ == "__main__":
    print(get_transactions_list("../data/operations.json"))
