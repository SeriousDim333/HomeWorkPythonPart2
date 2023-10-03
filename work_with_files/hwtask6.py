# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os


def rename_files(path, end_name, num, origin_extention, change_extention, start_num_name, end_num_name):
    os.chdir(path)
    list_files = os.listdir()
    count = 10**(num)
    for obj in list_files:
        *name, ext = obj.split(".")
        if ext == origin_extention:
            os.rename(obj, str(*name)[start_num_name:end_num_name] +
                      end_name+str(count)[1:]+change_extention)
            count += 1


if __name__ == '__main__':
    rename_files(r"python part 2\sem7\testt", "xxx", 2, "qw", ".we", 3, 6)
