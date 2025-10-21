def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера карты"""

    card_str = str(card_number)
    # Проверяем корректность длины номера карты
    if len(card_str) != 16:
        raise ValueError("Номер счета должен содержать 16 цифр")
    output_list = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
    return output_list


# print (get_mask_card_number (1234567891234567))


def get_mask_account(card_account: int) -> str:
    """Маскировка номера счета"""

    card_account_str = str(card_account)
    # Проверяем корректность длины номера счета
    if len(card_account_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    output_list = "**" + card_account_str[-4:]
    return output_list


# print (get_mask_account (1234567891234567))
