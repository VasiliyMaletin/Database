# и фиксацией времени, когда это было
# После нажатия кнопок Сохранить или Удалить, делается запись в лог с переданной строкой 
from datetime import datetime

def add_log(log_record):
    time = datetime.now().strftime('%H:%M:%S')
<<<<<<< HEAD
    with open('log.csv', 'a') as log:
        log.write('{} Действие: {}\n'
=======
    with open('log.csv', 'a', encoding='utf-8') as log:
        log.write('{} Action: {}\n'
>>>>>>> 9068be8205b6f903439570728824728349190c25
                    .format(time, log_record))

