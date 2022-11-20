import json

def request_filter_data_to_list(find_pupil): # Поиск ученика по заданному словарю.
    with open('pupils.json', 'r', encoding='utf-8') as file:
        list_pupils = json.load(file)
    pupil_list = []
    for i in list_pupils:
        check = 0
        if i["ФИО"] != " ":
            print(i["ФИО"])
            a = find_pupil["ФИО"]
            b = i["ФИО"]
            if a in b:
                check = 1
            else:
                check = 0
                continue

        if i["Класс"] != " ":
            print(i["Класс"])
            a = find_pupil["Класс"]
            b = i["Класс"]
            if a in b:
                check = 1
            else:
                check = 0
                continue

        if i["Руководитель"] != " ":
            print(i["Руководитель"])
            a = find_pupil["Руководитель"]
            b = i["Руководитель"]
            if a in b:
                check = 1
            else:
                check = 0
                continue

        if i["Успеваемость"] != " ":
            print(i["Успеваемость"])
            a = find_pupil["Успеваемость"]
            b = i["Успеваемость"]
            if a in b:
                check = 1
            else:
                check = 0
                continue

        if i["Год рождения"] != " ":
            print(i["Год рождения"])
            a = find_pupil["Год рождения"]
            b = i["Год рождения"]
            if a == b:
                check = 1
            else:
                check = 0
                continue

        if i["Телефон"] != " ":
            print(i["Телефон"])
            a = find_pupil["Телефон"]
            b = i["Телефон"]
            if a == b:
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

find_pupil = {"id": " ", "ФИО": "Иванов", "Класс": " ", "Руководитель": " ", "Успеваемость": " ", "Год рождения": 2012, "Телефон": " "}
print(request_filter_data_to_list(find_pupil))
