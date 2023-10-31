# Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".
# Ваша задача - написать набор тестов для класса Employee с использованием модуля doctest,
# чтобы убедиться, что он работает правильно.
# Тесты:
# test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov",
# именем "Ivan", отчеством "Ivanovich" и возрастом 30. Убедитесь, что метод full_name() возвращает правильное
# полное имя в формате "Ivanov Ivan Ivanovich".
# test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с фамилией "Ivanov",
# именем "Ivan", отчеством "Ivanovich" и возрастом 30. Вызовите метод birthday() и убедитесь, что возраст 
# увеличился на 1 и стал равным 31.
# test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с фамилией "Ivanov",
# именем "Ivan", отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Вызовите 
# метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
# test_employee_str: Тестирование метода __str__(). Создайте объект Employee с фамилией "Ivanov", именем
# "Ivan", отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Убедитесь, что 
# метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)"
# test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией
# "ivanov" (в нижнем регистре), именем "ivan" (в нижнем регистре), отчеством "ivanovich" (в нижнем регистре),
# возрастом 30, должностью "manager" и зарплатой 50000. Убедитесь, что атрибут last_name возвращается в 
# верхнем регистре, то есть "Ivanov". 


import doctest

class Person:
    '''
    >>> r = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
    >>> r.last_name
    'Ivanov'
    '''

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        '''
        >>> r = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> r.full_name()
        'Ivanov Ivan Ivanovich'
        '''
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        '''
        >>> r = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> r.birthday()
        >>> r.get_age()
        31
        '''
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        '''
        >>> r = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> r.raise_salary(10)
        >>> int(r.salary)
        55000
        '''
        self.salary *= (1 + percent / 100)

    def __str__(self):
        '''
        >>> r = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> print(r)
        Ivanov Ivan Ivanovich (Manager)
        '''
        return f'{self.full_name()} ({self.position})'
    
doctest.testmod(verbose=True)
# r = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
# r.raise_salary(10)
# r.birthday()
# print(int(r.salary))