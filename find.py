import json

def request_filter_data_to_list(find_pupil): # Поиск ученика по заданному словарю.
    with open('pupils.json', 'r', encoding='utf-8') as file:
        list_pupils = json.load(file)
    pupil_list = []
    for i in list_pupils:
        check = 0
        for j in find_pupil:
            if find_pupil[j] != "":
                if find_pupil[j] in i[j]:
                    check = 1
                else:
                    check = 0
                    continue

        if check == 1:
            pupil_list.append(i)
    return pupil_list

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