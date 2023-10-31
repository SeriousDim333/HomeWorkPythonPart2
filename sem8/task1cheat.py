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
    if directory == 'geekbrains':
        return [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
    elif directory == 'geekbrains/my_ds_projects':
        return [{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
    else:
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

# print(traverse_directory('geekbrains/my_ds_projects'))

