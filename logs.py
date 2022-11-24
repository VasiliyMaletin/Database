# и фиксацией времени, когда это было
# После нажатия кнопок Сохранить или Удалить, делается запись в лог с переданной строкой 
from datetime import datetime

def add_log(log_record):
    time = datetime.now().strftime('%H:%M:%S')
    with open('log.csv', 'a', encoding='utf-8') as log:
        log.write('{} Действие: {}\n'
                    .format(time, log_record))

