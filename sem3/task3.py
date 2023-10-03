# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

# campaign_staff = {"лапата": 2, "палатка": 4,
#                   "фляга": 1, "топор": 2, "спальник": 3, "еда": 6}

# weight = int(input("введите максимальный вес: "))

# for key, value in campaign_staff.items():
#     if weight-value >= 0:
#         print(key)
#         weight -= value

# Создайте словарь со списком вещей для похода в
# качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его
# максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант. Верните все возможные
# варианты комплектации рюкзака.
from itertools import permutations

MAX_WEIGHT = 10
THINGS = {
    'Лопата': 4,
    'Фонарь': 1,
    'Еда': 2,
    'Палатка': 7,
    'Колонка': 2,
    'Вода': 4,
    'Удочка': 3,
    'Мангал': 3,
    'Топор': 3,
}


def get_availaible_weight(things_set: set[str]) -> float:
    '''Получить доступный вес рюкзака.'''
    availaible = MAX_WEIGHT
    for i in things_set:
        availaible -= THINGS[i]
    return availaible


# создадим все возможные варианты
res = set()
current_w_availaible = MAX_WEIGHT
permut_things = permutations(THINGS.items())
# собираем все возможные по-максимуму заполненные рюкзаки
for thing_var in permut_things:
    current_w_availaible = MAX_WEIGHT
    temp_res = set()
    for thing, weight in thing_var:
        if weight <= current_w_availaible:
            temp_res.add(thing)
            current_w_availaible -= weight
    res.add(tuple(temp_res))

# создаем список кортежей вещи-вес
most_effective_list = []
for things in res:
    current_space = get_availaible_weight(things)
    print(f'{things}, Доступно {current_space}')
    most_effective_list.append((things, current_space))

# выведем самые оптимальные варианты
print()
print('Самые удачные варианты:')
most_effective = min(most_effective_list, key=lambda x: x[1])
most_effective_list = list(filter(lambda x: x[1] == most_effective[1],
                                  most_effective_list))
for value in most_effective_list:
    print(value)