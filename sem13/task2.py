# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст
# не является строкой или является пустой строкой.
# И InvalidNumberError, которое будет вызываться, если число не является положительным
# целым числом или числом с плавающей запятой.

from typing import Union


class MyExcept(Exception):
    pass


class InvalidTextError(MyExcept):
    def __init__(self, val) -> None:
        self.val = val


    def __str__(self) -> str:
        return f"Invalid text: {self.val}. Text should be a non-empty string."



class InvalidNumberError(MyExcept):
    def __init__(self, num) -> None:
        self.num = num

    def __str__(self) -> str:
        return f"Invalid number: {self.num}. Number should be a positive integer or float."

class CheckDijit:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and value>=0:
            setattr(instance, self.name, value)
        else:
            raise InvalidNumberError(value)
        
class CheckStr:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or value.strip()=="":
            raise InvalidTextError(value)
        else:
            setattr(instance, self.name, value)


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    number = CheckDijit()
    text = CheckStr()
    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# archive1 = Archive("First Text", 1)
# archive2 = Archive("Second Text", 2)
# archive3 = Archive("Third Text", 3)
# print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
# print(archive1.archive_number)  # Выведет: [1, 3]
# print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
# print(archive2.archive_number)

# archive_instance = Archive("Sample text", 42.5)
# print(archive_instance)

invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)


# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)
