# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит
# эту директорию и все вложенные директории. Результаты обхода должны быть сохранены в нескольких
# форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или
# директория. Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные
# файлы и директории в байтах. Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной
# директории, и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и
# возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных
# файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

import os
from pathlib import Path
import json
import csv
import pickle


def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # Если встретился не каталог, а файл, то вернётся его размер
        return os.path.getsize(directory)
    except PermissionError:
        # Если папка не открывается, вернётся 0
        return 0
    return total


def traverse_directory(directory):
    new_list = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            new_dict = {}
            if os.path.isfile(os.path.join(dirpath, file)):
                new_dict["Path"] = os.path.join(dirpath, file)
                new_dict["Type"] = "File"
                new_dict["Size"] = os.path.getsize(os.path.join(dirpath, file))
                new_list.append(new_dict)
        for dir in dirnames:
            new_dict = {}
            if os.path.isdir(os.path.join(dirpath, dir)):
                new_dict["Path"] = os.path.join(dirpath, dir)
                new_dict["Type"] = "Directory"
                new_dict["Size"] = get_directory_size(
                    os.path.join(dirpath, dir))
                new_list.append(new_dict)
    return new_list


def save_results_to_json(results, name_file):
    with open(name_file, "w", encoding="utf-8") as f:
        json.dump(results, f)


def save_results_to_csv(results, name_file):
    with open(name_file, "w", newline='', encoding="utf-8") as f:
        csv_write = csv.DictWriter(f, fieldnames=[
                                   "Path", "Type", "Size"])
        csv_write.writeheader()
        csv_write.writerows(results)


def save_results_to_pickle(results, name_file):
    with open(name_file, "wb") as f:
        pickle.dump(results, f)


print(traverse_directory(
     r"D:\обучение\python\python part 2\HomeWorkPart2\work_with_files\testt\geekbrains"))
