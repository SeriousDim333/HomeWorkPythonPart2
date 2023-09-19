# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

campaign_staff = {"лапата": 2, "палатка": 4,
                  "фляга": 1, "топор": 2, "спальник": 3, "еда": 6}

weight = int(input("введите максимальный вес: "))

for key, value in campaign_staff.items():
    if weight-value >= 0:
        print(key)
        weight -= value