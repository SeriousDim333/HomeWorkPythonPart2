# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный)
# имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст)
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные
# неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.
class InvalidNameError(Exception):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Invalid name: {self.name}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, age) -> None:
        self.age = age

    def __str__(self) -> str:
        return f"Invalid age: {self.age}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, id) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999."


class CheckStr:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or value.strip() == "":
            raise InvalidNameError(value)
        else:
            setattr(instance, self.name, value)


class Person:
    last_name = CheckStr()
    name = CheckStr()
    sur_name = CheckStr()

    def __init__(self, last_name, name, sur_name, age) -> None:
        self.last_name = last_name
        self.name = name
        self.sur_name = sur_name
        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            raise InvalidAgeError(age)
        
    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1

    def __repr__(self) -> str:
        return f'Person({self.last_name}, {self.name}, {self.sur_name}, {self.age})'


class Employee(Person):
    def __init__(self, last_name, name, sur_name, age, id) -> None:
        if 99_999 < id < 1_000_000:
            self.id = id
        else:
            raise InvalidIdError(id)
        super().__init__(last_name, name, sur_name, age)

    def get_level(self):
        return sum(map(int, str(self.id))) % 7

    def __repr__(self) -> str:
        return f'Employee({self.last_name}, {self.name}, {self.sur_name}, {self.age}, {self.id}, {Employee(self.last_name, self.name, self.sur_name, self.age, self.id).get_level()})'


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())