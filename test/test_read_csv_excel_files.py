from unittest.mock import patch

import pandas as pd

from src.read_csv_excel_files import read_excel_func


@patch('pandas.read_excel')
def test_open_file_excel(mock_read_excel):
    # Создаём DataFrame, который будет возвращать mock
    mock_data = {
        'id': [650703],
        'state': ['EXECUTED'],
        'date': ['2023-09-05T11:30:32Z'],
        'amount': [16210],
        'currency_name': ['Sol'],
        'currency_code': ['PEN'],
        'from': ['Счет 58803664561298323391'],
        'to': ['Счет 39745660563456619397'],
        'description': ['Перевод организации']
    }
    mock_df = pd.DataFrame.from_dict(mock_data)
    mock_read_excel.return_value = mock_df

    expected_result = [
        {
            'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]

    result = read_excel_func('dummy_path.xlsx')
    assert result == expected_result
