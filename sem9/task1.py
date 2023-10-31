# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать
# по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
# Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного
# уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит
# параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json
# будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

import json
import csv
from random import randint


def save_to_json(func):
    def wrapper(*args):
        with open(args[0], "r") as f:
            data = csv.reader(f)
            new_dict = []
            for line in data:
                a, b, c = line
                res = func(a, b, c)
                new_dict.append({f'{a},{b},{c}': res})
        with open("results.json", "w") as f:
            json.dump(new_dict, f, indent=2, separators=(',', ':'))
    return wrapper


def generate_csv_file(file_name, rows):
    with open(file_name, "w", newline="") as f:
        csv_write = csv.writer(f, dialect='excel')
        for i in range(rows):
            if i == rows-1:
                csv_write = csv.writer(f, dialect='excel', lineterminator="")
                a = randint(1, 100)
                b = randint(1, 100)
                c = randint(1, 100)
                csv_write.writerow([a, b, c])
            else:
                a = randint(1, 100)
                b = randint(1, 100)
                c = randint(1, 100)
                csv_write.writerow([a, b, c])


@save_to_json
def find_roots(*args):
    a, b, c = map(int, args)
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2


# generate_csv_file("numbers.csv", 100)
# find_roots("numbers.csv")
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)