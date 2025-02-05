import json
import os


def read_json_transactions(file_path: str) -> list:
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    param: file_path: str, путь к JSON-файлу
    :return: list, список словарей с финансовыми транзакциями или пустой список
    """
    if not os.path.isfile(file_path):
        return []

    # Пытаемся открыть и прочитать JSON-файл
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            # Проверяем, содержит ли данные список
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        # Если файл пустой, поврежден или другая ошибка, возвращаем пустой список
        return []
