import unittest
from unittest.mock import patch

import pandas as pd

from src.csv_excel import read_financial_operations_excel


@patch("pandas.read_excel")
def test_read_financial_operations_excel(mock_read_excel):
    # Создаем фейковые данные в виде DataFrame
    mock_data = pd.DataFrame(
        {
            "id": [123, 456],
            "state": ["EXECUTED", "CANCELED"],
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [1000, 2000],
            "currency_name": ["USD", "EUR"],
            "currency_code": ["USD", "EUR"],
            "from": ["Account 1", "Account 2"],
            "to": ["Account 3", "Account 4"],
            "description": ["Test transaction 1", "Test transaction 2"],
        }
    )

    # Настраиваем mock на возврат созданного DataFrame
    mock_read_excel.return_value = mock_data

    # Вызываем тестируемую функцию
    file_path = "dummy_path.xlsx"
    transactions = read_financial_operations_excel(file_path)

    # Ожидаемые результаты
    expected_transactions = [
        {
            "id": 123,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "amount": 1000,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Account 1",
            "to": "Account 3",
            "description": "Test transaction 1",
        },
        {
            "id": 456,
            "state": "CANCELED",
            "date": "2023-01-02",
            "amount": 2000,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "Account 2",
            "to": "Account 4",
            "description": "Test transaction 2",
        },
    ]

    # Проверяем, что функция вернула ожидаемые результаты
    assert transactions == expected_transactions

    # Проверяем, что read_excel была вызвана с правильным аргументом
    mock_read_excel.assert_called_once_with(file_path)


if __name__ == "__main__":
    unittest.main()
