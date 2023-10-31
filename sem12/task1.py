# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию,выведите:
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Если такого предмета нет, выведите:
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:
# Оценка должна быть целым числом от 2 до
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
# Математика,Физика,История,Литератур
# Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
# Атрибуты класса
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и
# информацию об оценках и результатах тестов для каждого предмета в виде словаря.
# Магические методы (Dunder-методы)
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
# Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается
# с заглавной буквы и состоит только из букв.
# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
# Методы класса:
# load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из
# файла и добавляет предметы в атрибут subjects.
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым
# числом от 2 до 5.
# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается,
# что результат теста является целым числом от 0 до 100.
# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
# get_average_grade(self): Возвращает средний балл по всем предметам.
# import csv


# class CheckName:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if value.istitle() and value.replace(" ", "").isalpha():
#             setattr(instance, self.name, value)
#         # else:
#         #     print("ФИО должно состоять только из букв и начинаться с заглавной буквы")


# class Student:
#     name = CheckName()

#     def __init__(self, name, subjects_file):
#         self.name = name
#         self.subjects = self.load_subjects(subjects_file)

#     def load_subjects(self, subjects_file):
#         with open(subjects_file, "r", newline="", encoding="utf-8") as f:
#             data = csv.reader(f, delimiter=',')
#             for line in data:
#                 obj = line
#             subjects = {}
#             for i in obj:
#                 subjects[i] = {"test_score": [], "grades": []}
#             return subjects

#     def __str__(self):
#         result = ""
#         for keys, values in self.subjects.items():
#             if self.subjects[keys]["test_score"] or self.subjects[keys]["grades"]:
#                 result += keys+", "
#         return f'Студент: {self.name}\nПредметы: {result[:-2]}'

#     def add_grade(self, subject, grade):
#         if isinstance(grade, int) and 1 < grade < 6:
#             if subject in self.subjects:
#                 self.subjects[subject]["grades"].append(grade)
#             else:
#                 print(f"Предмет {subject} не найден")
#         # else:
#         #     print("Оценка должна быть целым числом от 2 до 5")

#     def add_test_score(self, subject, test_score):
#         if isinstance(test_score, int) and 0 <= test_score < 101:
#             if subject in self.subjects:
#                 self.subjects[subject]["test_score"].append(test_score)
#             else:
#                 print(f"Предмет {subject} не найден")
#         else:
#             print("Результат теста должен быть целым числом от 0 до 100")

#     def get_average_test_score(self, subject):
#         if subject in self.subjects:
#             return sum(self.subjects[subject]["test_score"])/len(self.subjects[subject]["test_score"])
#         else:
#             raise ValueError(f"Предмет {subject} не найден")


#     def get_average_grade(self):
#         new_list = []
#         for i in self.subjects:
#             for j in self.subjects[i]["grades"]:
#                 new_list.append(j)
#         return sum(new_list)/len(new_list)


# student = Student("123 Иван", "obj.csv")


import csv

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - __init__(self, name, subjects_file): конструктор класса
    - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - __getattr__(self, name): получение значения атрибута
    - __str__(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)


    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}
    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)

student = Student("123 Иван", "obj.csv")