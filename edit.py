import json
from logs import add_log
# from interface import get_pupil_dict
from find import request_all_data_to_list, request_pupil_data
id = 2
temp_pupil_dict = {"id": 2, "ФИО": "Петров Иван Иванович", "Класс": "10В", "Руководитель": "Сидоренко Арина Николаевна", "Успеваемость": "Хорошист", "Год рождения": "2011", "Телефон": "89174455584"}
def save_data(save_pupil_dict):
    pupil_dict = request_all_data_to_list()
    id_found = False
    for i in range(len(pupil_dict)):
        if save_pupil_dict["id"] == pupil_dict[i]["id"]:
            pupil_dict[i] = save_pupil_dict
            id_found = True
    if id_found == False:
        pupil_dict.append(save_pupil_dict)
    with open('pupils.json', 'w', encoding='utf-8') as file:
                json.dump(pupil_dict, file, ensure_ascii=False)
    if id_found == False:
         add_log(f'Новый ученик с id {save_pupil_dict["id"]} успешно добавлен')
    else:
        add_log(f'Изменения в id {save_pupil_dict["id"]} успешно сохранены')

    # new_pupil_dict = request_pupil_data(id)
    # for index, key in enumerate(pupil_dict):
    #     if key["id"] == temp_pupil_dict["id"]:
            # temp = temp_pupil_dict
            # temp.append(data_new)
            # key['data'] = temp
            # data[index] = key
            # break

            # обновить данные в json файл по id данными из pupil_dict
            # pupil_list = request_all_data_to_list()
            # print(pupil_list)
            
        # else:
        #     pupil_dict = temp_pupil_dict
            # добавить новую строку в json файл из pupil_dict
    


    # Переписать словарь ученика с указанным id (Есть в pupil_dict) новыми данными из pupil_dict в json файле
    # Если записи с указанным id не существует, создать эту новую запись с переданными данными

    # listbox_fill(pupil_dict)
    # print(f'Изменения сохранены по id {pupil_dict["id"]}')
   