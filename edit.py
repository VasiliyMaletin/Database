import json
from logs import add_log
from find import request_all_data_to_list, request_pupil_data

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