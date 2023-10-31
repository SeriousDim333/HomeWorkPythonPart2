# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют
# дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию
# глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
# (Малявка, Обычный, Гигант) в зависимости от веса.
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе
# переданного типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal'). *args - переменное количество аргументов,
# представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости
# от типа животного. Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными
# параметрами.

class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan/2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "мелководная рыба"
        elif 10 < self.max_depth < 60:
            return "Средневодная рыба"
        else:
            return "глубоководная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 10:
            return "Малявка"
        elif 10 < self.weight < 100:
            return "Обычный"
        else:
            return "Гигант"


class AnimalFactory:

    def create_animal(type_a, *args):
        animal_dict = {'Bird': Bird, 'Fish': Fish, 'Mammal': Mammal}
        if type_a in animal_dict:
            new_animal = animal_dict[type_a](*args)
            return new_animal
        else:
            raise ValueError('Недопустимый тип животного')


# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())

animal1 = AnimalFactory.create_animal('Bird', 'Eagle', 200)
print(animal1.wing_length())

animal2 = AnimalFactory.create_animal('Fish', 'Salmon', 50)
print(animal2.depth())

animal4 = AnimalFactory.create_animal('Spider', 'Elephant', 5000)
print(animal4.category())  # ValueError: Недопустимый тип животного

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan

#     def wing_length(self):
#         return self.wingspan / 2

# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         super().__init__(name)
#         self.max_depth = max_depth

#     def depth(self):
#         if self.max_depth < 10:
#             return 'Мелководная рыба'
#         elif self.max_depth > 100:

#             return 'Глубоководная рыба'
#         return 'Средневодная рыба'

# class Mammal(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         self.weight = weight

#     def category(self):
#         if self.weight < 1:
#             return 'Малявка'
#         elif self.weight > 200:
#             return 'Гигант'
#         return 'Обычный'

# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type, *args):
#         if animal_type == 'Bird':
#             return Bird(*args)
#         elif animal_type == 'Fish':
#             return Fish(*args)
#         elif animal_type == 'Mammal':
#             return Mammal(*args)
#         else:
#             raise ValueError('Недопустимый тип животного')
