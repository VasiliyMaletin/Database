from logs import add_log

def save_data(pupil_dict):
    # Переписать словарь ученика с указанным id (Есть в pupil_dict) новыми данными из pupil_dict в json файле
    # Если записи с указанным id не существует, создать эту новую запись с переданными данными
    add_log(f'Изменения сохранены по id {pupil_dict["id"]}')
    pass