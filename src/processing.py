dictionnary_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dictionnary_list: list, state) -> list:
    """Фильтрация словарей по признаку EXECUTED"""

    return [i for i in dictionnary_list if i["state"] == "EXECUTED"]


filter_by_state(dictionnary_list, state="EXECUTED")


def sort_by_date(dictionnary_list: list, ascending=False) -> list:
    """Сортировка по дате"""

    sorted_list = sorted(dictionnary_list, key=lambda list_: list_.get("date", 0), reverse=True)
    return sorted_list


# sorted_new_list = sort_by_date(dictionnary_list)
# print(sorted_new_list)
