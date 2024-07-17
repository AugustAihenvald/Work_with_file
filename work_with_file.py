from csv import DictWriter, DictReader
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 5:
                raise NameError("Слишком короткая фамилия")
        except NameError as err:
            print(err)
        else:
            flag = True
    phone = "+73287282037"
    return [first_name, last_name, phone]

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standart_write(filename, res)

def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена!"

def delet_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    res.pop(row_number-1)
    standart_write(filename, res)


def standart_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def alter_row(filename):
    row_number = int(input("Введите номер строки для изменения: "))
    res = read_file(filename)
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standart_write(filename, res)

def copy_row(filename, second_file):
    row_number = int(input("Введите номер строки для копирования: "))
    res = read_file(filename)
    obj = res[row_number-1]
    res_2 = read_file(second_file)
    res_2.append(obj)
    standart_write(second_file, res_2)

    

filename = 'phone.csv'
second_file = 'phone_2.csv'

def main():
    while True:
        command = input("Введите команду (q - выход, w - запись, r - чтение, f - найти пользователя по фамилии, d - удалить строку по индексу, a - внести изменения в строку, с - копировать и перенести строку в другой файл): ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(read_file(filename))
        elif command == "f":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command == "d":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delet_row(filename)
        elif command == "a":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            alter_row(filename)
        elif command == 'c':
            if not exists(second_file):
                print("Файл не существует. Создайте его.")
                create_file(second_file)
                continue
            copy_row(filename, second_file)

main()