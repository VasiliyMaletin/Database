import json
from logs import add_log

def pupil_add():
    with open('pupils.json', 'r', encoding='utf-8') as file:
        list_pupils = json.load(file)
    max = 0
    for pupil in list_pupils:
        if pupil["id"] > max:
            max = pupil["id"] 
            new_id = max + 1
    return new_id


def pupil_delete(id):
    with open('pupils.json', 'r', encoding='utf-8') as file:
        list_pupils = json.load(file)
    for i in range(len(list_pupils)):
        if list_pupils[i]['id'] == id:
            list_pupils.pop(i)
            break

    with open('pupils.json', 'w', encoding='utf-8') as file:
        json.dump(list_pupils, file, ensure_ascii=False)
    add_log(f'Ученик с id {id} был удален')


        

   