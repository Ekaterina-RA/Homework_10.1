
from typing import Dict, List


def filter_by_state(list_dict: List[Dict], key: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и значение ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий словари соответствующих ключу"""
    new_list = []
    for each_dict in list_dict:
        if each_dict["state"] == key:
            new_list.append(each_dict)
    return new_list



def sort_by_date(list_dict: List[Dict], sort_arg: bool = True) -> List[Dict]:
    """Принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате"""
    sort_list = sorted(list_dict, key=lambda each_dict: each_dict["date"], reverse=sort_arg)
    return sort_list