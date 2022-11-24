from tkinter import *
from tkinter.messagebox import showinfo
from find import request_filter_data_to_list, request_all_data_to_list, request_pupil_data
from edit import save_data
from add_delete import pupil_add, pupil_delete

# # При загрузке окна, выводим все данные в список учеников find.
# request_all_data_to_list() # Возвращает список словарей.

# # При выборе ученика делаем запрос по данным на этого ученика в модуль find. Распределить данные по полям
# request_pupil_data(id) # На вход число id (именно число, не строка). Возвращает словарь ученика.

# # Кнопка редактировать делает доступным для изменния все поля с данными
# # Кнопка сохранить отправляет данные из полей в edit.py для записи их в БД + Заново вывод 
# save_data(pupil_dict)
# request_all_data_to_list # Возвращает список словарей.

# # Кнопки фильтров вызывают request_filter_data_to_list с указанием имени поля фильтрации и данных
# list=request_filter_data_to_list(find_pupil) # На вход словарь. Возвращает список словарей.

# # Кнопка добавить делает запрос и получает id нового ученика, заполняет его в поле id, очищает все поля с данными, 
# # запускает режим редактирования этого нового ученика
# new_id=pupil_add()
# pupil_delete(id)

# # Редактирование данных нового ученика пользоваетелем
# save_data(pupil_dict)

# Список для хранения id учеников
global pupil_listbox
global pupil_id_list


pupil_id_list = []
pupil_filter_dict = {"id": "", "ФИО": "", "Класс": "", "Руководитель": "", "Успеваемость": "", "Год рождения": "", "Телефон": ""}

# Создание словаря с данными по ученику из текущих данных информационных полей
def get_pupil_dict():
    temp_pupil_dict  =  {"id": 0, "ФИО": "", "Класс": "", "Руководитель": "", "Успеваемость": "", "Год рождения": "", "Телефон": ""}
    temp_pupil_dict["id"] = int(id_textbox.get())
    temp_pupil_dict["ФИО"] = fio_textbox.get()
    temp_pupil_dict["Класс"] = class_textbox.get()
    temp_pupil_dict["Руководитель"] = class_boss_textbox.get()
    temp_pupil_dict["Успеваемость"] = score_textbox.get()
    temp_pupil_dict["Год рождения"] = birthday_textbox.get()
    temp_pupil_dict["Телефон"] = phone_textbox.get()
    return temp_pupil_dict

# Очистка данных во всех полях
def textbox_clear_data():
    id_textbox.delete(0, "end")
    fio_textbox.delete(0, "end")
    class_textbox.delete(0, "end")
    class_boss_textbox.delete(0, "end")
    score_textbox.delete(0, "end")
    birthday_textbox.delete(0, "end")
    phone_textbox.delete(0, "end")
                        
# Обработка выбора ученика в ListBox
def onselect(event):
    global pupil_id_list
    global pupil_dict
    
    w = event.widget
    if w.curselection() != ():
        index = int(w.curselection()[0])
        id = pupil_id_list[index]
        pupil_dict = request_pupil_data(id)
        
        id_textbox.delete(0,"end")
        id_textbox.insert(0, pupil_dict["id"])
        
        fio_textbox.config(state="normal")
        fio_textbox.delete(0, "end")
        fio_textbox.insert(0, pupil_dict["ФИО"])
        fio_textbox.config(state="readonly")
        
        class_textbox.config(state="normal")
        class_textbox.delete(0, "end")
        class_textbox.insert(0, pupil_dict["Класс"])
        class_textbox.config(state="readonly")
        
        class_boss_textbox.config(state="normal")
        class_boss_textbox.delete(0, "end")
        class_boss_textbox.insert(0, pupil_dict["Руководитель"])
        class_boss_textbox.config(state="readonly")
        
        score_textbox.config(state="normal")
        score_textbox.delete(0, "end")
        score_textbox.insert(0, pupil_dict["Успеваемость"])
        score_textbox.config(state="readonly")
        
        birthday_textbox.config(state="normal")
        birthday_textbox.delete(0, "end")
        birthday_textbox.insert(0, pupil_dict["Год рождения"])
        birthday_textbox.config(state="readonly")
        
        phone_textbox.config(state="normal")
        phone_textbox.delete(0, "end")
        phone_textbox.insert(0, pupil_dict["Телефон"])
        phone_textbox.config(state="readonly")
    
def save_button_click(event):
    save_pupil_dict = get_pupil_dict()
    save_data(save_pupil_dict)
    edit_button.grid()
    add_button.grid()
    delete_button.grid()
    save_button.grid_remove()
    search_button.grid()
    all_button.grid()
    fio_textbox.config(state="readonly")
    class_textbox.config(state="readonly")
    class_boss_textbox.config(state="readonly")
    score_textbox.config(state="readonly")
    birthday_textbox.config(state="readonly")
    phone_textbox.config(state="readonly")
    pupil_listbox.config(state=NORMAL)
    show_all_click("")


def add_button_click(event):
    new_id = pupil_add()
    edit_button_click(event)
    textbox_clear_data()
    id_textbox.insert(0, new_id)

def delete_button_click(event):
    pupil_id_delete = int(id_textbox.get())
    pupil_delete(pupil_id_delete)
    show_all_click("")


def edit_button_click(event):
    edit_button.grid_remove()
    add_button.grid_remove()
    delete_button.grid_remove()
    save_button.grid()
    search_button.grid_remove()
    all_button.grid_remove()
    fio_textbox.config(state="normal")
    class_textbox.config(state="normal")
    class_boss_textbox.config(state="normal")
    score_textbox.config(state="normal")
    birthday_textbox.config(state="normal")
    phone_textbox.config(state="normal")
    pupil_listbox.config(state=DISABLED)

def search_button_click(event):
    edit_button.grid_remove()
    add_button.grid_remove()
    delete_button.grid_remove()
    find_button.grid()
    search_button.grid_remove()
    all_button.grid_remove()
    fio_textbox.config(state="normal")
    class_textbox.config(state="normal")
    class_boss_textbox.config(state="normal")
    score_textbox.config(state="normal")
    birthday_textbox.config(state="normal")
    phone_textbox.config(state="normal")
    pupil_listbox.config(state=DISABLED)
    textbox_clear_data()


def find_button_click(event):
    filtered_list = request_filter_data_to_list(get_pupil_dict())
    edit_button.grid()
    add_button.grid()
    delete_button.grid()
    find_button.grid_remove()
    search_button.grid()
    all_button.grid()
    textbox_clear_data()
    fio_textbox.config(state="readonly")
    class_textbox.config(state="readonly")
    class_boss_textbox.config(state="readonly")
    score_textbox.config(state="readonly")
    birthday_textbox.config(state="readonly")
    phone_textbox.config(state="readonly")
    pupil_listbox.config(state=NORMAL)
    listbox_fill(filtered_list)

def show_all_click(event):
    listbox_fill(request_all_data_to_list())


def listbox_fill(cur_pupil_dict):
    global pupil_listbox
    global pupil_id_list
    
    pupil_listbox.delete(0, 'end')
    pupil_id_list = []
    for i in range(len(cur_pupil_dict)):
        pupil_id_list.append(cur_pupil_dict[i]["id"])
        pupil_listbox.insert(END, cur_pupil_dict[i]["ФИО"])
    
    
def window_init():
    global pupil_listbox
    global pupil_id_list
    global id_textbox
    global fio_textbox
    global class_textbox
    global class_boss_textbox
    global score_textbox
    global birthday_textbox
    global phone_textbox
    global add_button
    global delete_button
    global edit_button
    global save_button
    global search_button
    global find_button
    global all_button

    common_font = ("Courier", 14)
    bold_font = ("Courier", 14, "bold")
    
    # Задание начальных данных по окну
    root = Tk()
    root.title("Информация по ученикам")
    root_width = 1000
    root_height = 400
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    
    # Расчет координат окна, чтобы при выводе оно оказалось по центру экрана
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - root_width) / 2
    y = (sh - root_height) / 2
    
    # Задание размеров окна и его начального положения при выводе   
    root.geometry(f"{root_width}x{root_height}+{int(x)}+{int(y)}")

    # Создание подписей и текстовых полей для отображения данных по ученикам
    id_textbox = Entry(font=common_font, justify=LEFT)
    
    pupil_data_label = Label(root, text="Информация по выбранному ученику", justify=CENTER, font=bold_font)
    pupil_data_label.grid(row=0, column=0, columnspan=2, sticky="ewns", padx=5, pady=5)
    
    pupil_list_label = Label(root, text="Ученики", justify=CENTER, font=bold_font)
    pupil_list_label.grid(row=0, column=2, sticky="ewns", padx=5, pady=5)
    
    fio_label = Label(root, text="ФИО ученика", justify=LEFT, font=common_font)
    fio_label.grid(row=1, column=0, sticky="wns", padx=5, pady=5)
    fio_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    fio_textbox.grid(row=1, column=1, sticky="wns", padx=5, pady=5)
    
    class_label = Label(root, text="Класс ученика", justify=LEFT, font=common_font)
    class_label.grid(row=2, column=0, sticky="wns", padx=5, pady=5)
    class_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    class_textbox.grid(row=2, column=1, sticky="wns", padx=5, pady=5)
    
    class_boss_label = Label(root, text="Классный руководитель", justify=LEFT, font=common_font)
    class_boss_label.grid(row=3, column=0, sticky="wns", padx=5, pady=5)
    class_boss_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    class_boss_textbox.grid(row=3, column=1, sticky="wns", padx=5, pady=5)
    
    score_label = Label(root, text="Успеваемость", justify=LEFT, font=common_font)
    score_label.grid(row=4, column=0, sticky="wns", padx=5, pady=5)
    score_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    score_textbox.grid(row=4, column=1, sticky="wns", padx=5, pady=5)
    
    birthday_label = Label(root, text="Дата рождения", justify=LEFT, font=common_font)
    birthday_label.grid(row=5, column=0, sticky="wns", padx=5, pady=5)
    birthday_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    birthday_textbox.grid(row=5, column=1, sticky="wns", padx=5, pady=5)
    
    phone_label = Label(root, text="Телефон", justify=LEFT, font=common_font)
    phone_label.grid(row=6, column=0, sticky="wns", padx=5, pady=5)
    phone_textbox = Entry(root, justify=LEFT, width=30, state="readonly", font=common_font)
    phone_textbox.grid(row=6, column=1, sticky="wns", padx=5, pady=5)
    
    # Создание Listbox со ScrollBar для вывода информации по всем ученикам
    scrollbar = Scrollbar(root)
    scrollbar.grid(row=1, column=2, rowspan=6, sticky="ens")
    pupil_listbox = Listbox(root, justify=LEFT, font=common_font)
    pupil_listbox.config(yscrollcommand=scrollbar.set, width=40)
    scrollbar.config(command=pupil_listbox.yview)
    pupil_listbox.grid(row=1, column=2, rowspan=6, sticky="news", padx=20, pady=5)
    pupil_listbox.bind('<<ListboxSelect>>', onselect)
    
    # Создание управляющих кнопок
    add_button = Button(root, font=common_font, text='Добавить ученика')
    add_button.bind(f'<Button>', add_button_click)
    add_button.configure(bg="Aquamarine")
    add_button.grid(column=0, row=7, sticky="news", padx=10, pady=10)
    
    delete_button = Button(root, font=common_font, text='Удалить ученика')
    delete_button.bind(f'<Button>', delete_button_click)
    delete_button.configure(bg="LightCoral")
    delete_button.grid(column=0, row=8, sticky="news", padx=10, pady=5)
    
    edit_button = Button(root, font=common_font, text='Редактировать данные')
    edit_button.bind(f'<Button>', edit_button_click)
    edit_button.configure(bg="Khaki")
    edit_button.grid(column=1, row=7, sticky="news", padx=10, pady=10)
    
    save_button = Button(root, font=common_font, text='Сохранить данные')
    save_button.bind(f'<Button>', save_button_click)
    save_button.configure(bg="Aquamarine")
    save_button.grid(column=1, row=7, sticky="news", padx=10, pady=10)
    save_button.grid_remove()
    
    search_button = Button(root, font=common_font, text='Поиск по данным')
    search_button.bind(f'<Button>', search_button_click)
    search_button.configure(bg="Khaki")
    search_button.grid(column=1, row=8, sticky="news", padx=10, pady=5)
    
    find_button = Button(root, font=common_font, text='Найти')
    find_button.bind(f'<Button>', find_button_click)
    find_button.configure(bg="Khaki")
    find_button.grid(column=1, row=8, sticky="news", padx=10, pady=5)
    find_button.grid_remove()
    
    all_button = Button(root, font=common_font, text='Показать всех')
    all_button.bind(f'<Button>', show_all_click)
    all_button.configure(bg="Aquamarine")
    all_button.grid(column=2, row=7, sticky="news", padx=30, pady=10)
    
    show_all_click("")
   
    # Вывод всего, что отрисовали на окне на экран и начало отслеживания событий всех элементов
    root.mainloop()