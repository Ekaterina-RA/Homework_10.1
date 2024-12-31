from processing import filter_by_state, sort_by_date
from typing import Dict, List

# Пример использования def filter_by_state:
list_dict= [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]

# Выход функции со статусом по умолчанию 'EXECUTED'
executed_items = filter_by_state(list_dict)
print(executed_items)

# Выход функции, если вторым аргументом передано 'CANCELED'
canceled_items = filter_by_state(list_dict, key='CANCELED')
print(canceled_items)

sorted_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
print(sorted_list)