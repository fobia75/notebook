


# записная книга
# студент Бутырин Владимир
import os
import sys

def add_new_user(name: str, phone: str, filename: str):
    """
    добавление нового пользователя
    """
    new_line = '\n' if read_all(file_name) != '' else ''
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{new_line}{name} - {phone}')


def read_all(filename: str) -> str:
    """
    считывает весь файл
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def search_user(file_name: str, data: str) -> str:
    """
    поиск юзера
    """ 
    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        list_1 = file.read().split('\n')
    for i in list_1:
        if data in i:
            result.append(i)
    if not result:
        return 'данные не найдены'       
    return '\n'.join(result)


def transfer_data(sourse: str, dest: str, num_row: str):
    """
    функция для переноса указанной строки из одного файла в другой
    sourse: str - имя исходного файла
    dest: str - имя конечного файла 
    num_row: str -  переносимая строка 
    """
    name_ = ()
    phone_ = ()
    str_ = ()
    if search_user(sourse, num_row):
        str_ = search_user(sourse, num_row)
        str_ = str_.split('\n')
        for i in str_:
            str_ = i
            continue
        name_, phone_ = str_.split('-') 
    new_line = '\n' if read_all(file_name) != '' else ''
    with open(dest, 'a', encoding='utf-8') as file:
        file.write(f'{new_line}{name_} - {phone_}')    


file_name = 'number.txt'
if file_name not in os.listdir():
    print('файл не найден')
    sys.exit()
INFO_STRING = """
Выберите режим работы
1-вывести все данные
2-добавление нового пользователя
3-поиск
4-перенос записи в другой файл
""" 
while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file_name))
    elif mode == 2:
        name = input('напишите имя:')
        phone = input('напишите номер телефона:')
        add_new_user(name, phone, file_name)    
    elif mode == 3:
        data = input('введите имя для поиска:')
        print(search_user(file_name, data))
    elif mode == 4:
        num_row = input('строку с каким именем вы хотите перенести:')
        sourse = input('из какого файла:')
        if sourse  not in os.listdir():
            print('файл с таким именем не найден')
            sys.exit()
        dest = input('в какой файл:')
        if dest  not in os.listdir():
            print('файл с таким именем не найден')
            sys.exit()
        transfer_data(sourse, dest, num_row)   