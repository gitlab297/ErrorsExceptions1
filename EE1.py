filename = '000.222'
a = 5
b = 0
lst = [1, 2, 5]
index = 5

def string_to_int(s):
    try:
       return int(s)
    except ValueError:
        return f'Ошибка. Невозможно преобразовать {s} в целое число'


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Ошибка. Файл {filename} не найден'
    except IOError:
        return f'Ошибка ввода/вывода при работе с файлом {filename}'


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка. Деление на ноль'
    except TypeError:
        return 'Ошибка. Аргументы должны быть числами'


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне диапазона списка'
    except TypeError:
        return 'Ошибка. Индекс должен быть целым числом'

print(string_to_int('fff'))
print(read_file(filename))
print(divide_numbers(a, b))
print(access_list_element(lst, index))
