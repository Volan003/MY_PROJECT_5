import logging
import os

logger = logging.getLogger('masks')
os.makedirs(os.path.join(os.getcwd(), 'logs'), exist_ok=True)
file_handler = logging.FileHandler('logs/masks.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера карты"""
    logger.info('Начало работы программы - Маскировка номера карты')
    card_str = str(card_number)
    # Проверяем корректность длины номера карты

    if len(card_str) != 16:
        logger.error(f'Произошла ошибка: Номер {card_number} должен содержать 16 цифр')
        raise ValueError("Номер карты должен содержать 16 цифр")
    logger.info('Окончание работы программы - Вывод маскированного номера карты')
    output_list = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
    return output_list

#print (get_mask_card_number (1234567891234567))


def get_mask_account(card_account: int) -> str:
    """Маскировка номера счета"""
    logger.info('Начало работы программы - Маскировка номера счета')
    card_account_str = str(card_account)
    # Проверяем корректность длины номера счета

    if len(card_account_str) != 20:
        logger.error(f'Произошла ошибка: Номер {card_account} должен содержать 20 цифр')
        raise ValueError("Номер счета должен содержать 20 цифр")
    logger.info('Окончание работы программы - Вывод маскированного номера счета')
    output_list = "**" + card_account_str[-4:]
    return output_list


# print (get_mask_account (1234567891234567))
#file_handler.close()
