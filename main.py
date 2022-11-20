from tkinter import *


def window_init():
    main_window = Tk()
    main_window.title("Данные учеников")
    main_window.geometry("600x600") 
    frame = Frame(borderwidth=1, relief=SOLID)
    label_id=Label(main_window, text="Код ученика")
    label_id.pack(anchor=NW, padx=10, pady=5)
    label_fio=Label(main_window, text="Фамилия, имя, отчество")
    label_fio.pack(anchor=NW, padx=10, pady=5)
    label_class=Label(main_window, text="Класс")
    label_class.pack(anchor=NW, padx=10, pady=5)
    label_class_ruk=Label(main_window, text="Классный руководитель")
    label_class_ruk.pack(anchor=NW, padx=10, pady=5)
    label_grades=Label(main_window, text="Оценки ученика")
    label_grades.pack(anchor=NW, padx=10, pady=5)
    label_birthday=Label(main_window, text="Дата рождения ученика")
    label_birthday.pack(anchor=NW, padx=10, pady=5)
    label_phone=Label(main_window, text="Номер ученика")
    label_phone.pack(anchor=NW, padx=10, pady=5)
    frame.pack(anchor=NE, fill=X, padx=5, pady=5)
 
    editor_id = Text()
    editor_id.pack(anchor=NE, padx=10, pady=5)   
 
    main_window.mainloop()
    
window_init()