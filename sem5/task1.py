# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# file_path = "C:/Users/User/Documents/example.txt"
# ('C:/Users/User/Documents/', 'example', '.txt')
# file_path = '/home/user/data/file'
# file_path = '/home/user/docs/my.file.with.dots.txt'

# def get_file_info(file_path):
#     result = []
#     *path, name = file_path.split("/")
#     *name, file = name.split(".")
#     if path == []:
#         result.append(str("/".join(path)))
#     else:
#         result.append(str("/".join(path)+'/'))
#     result.append(str(".".join(name)))
#     result.append("."+file)
#     return tuple(result)


# file_path = '/home/user/docs/my.file.with.dots.txt'
# print(get_file_info(file_path))

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    print(file_name)
    file_extension = file_name.split(".")[-1]
    print(file_extension)
    path = file_path[:-len(file_name)]
    print(path)
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

file_path = '/home/user/docs/my.file.with.dots.txt'
print(get_file_info(file_path))