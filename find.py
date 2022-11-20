import json

# def request_filter_data_to_list(find_pupil): # Поиск ученика по заданному словарю.
#     with open('pupils.json', 'r', encoding='utf-8') as file:
#         list_pupils = json.load(file)
#
#     pupil_list = []
#     return pupil_list

def request_all_data_to_list(): # Возвращает полный список учеников
    with open('pupils.json', 'r', encoding='utf-8') as file:
        pupil_list = json.load(file)
    return pupil_list

def request_pupil_data(id): # Возвращает словарь данных по конкретному ученику по его id
    with open('pupils.json', 'r', encoding='utf-8') as file:
        pupil_list = json.load(file)
    for i in pupil_list:
        if i["id"] == id:
            pupil_dict = i
    return pupil_dict

# print(request_pupil_data(1))
