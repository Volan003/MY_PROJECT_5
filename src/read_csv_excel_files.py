from typing import Any

import pandas as pd


def read_csv_func(path: str) -> list[Any]:
    """Функция чтения файла формата csv"""
    try:
        df = pd.read_csv(path)
        result = df.to_dict(orient='records')
        return result
    except FileNotFoundError:
        print('Файл не найден')


def read_excel_func(path: str) -> list[Any]:
    """Функция чтения файла формата excel"""
    try:
        df = pd.read_excel(path)
        result = df.to_dict(orient='records')
        return result
    except FileNotFoundError:
        print('Файл не найден')
