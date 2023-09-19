#  В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# Ввод:
# текст отсюда(https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81)
# Вывод:
# Слово "в", 22 раз
# Слово "и", 11 раз
# Слово "году", 9 раз
# Слово "с", 4 раз
# Слово "морли", 4 раз
# Слово "по", 3 раз
# Слово "степень", 3 раз
# Слово "института", 3 раз
# Слово "был", 3 раз
# Слово "памятников", 3 раз

import string

text = input("введите текст: ")
new_dict = {}
text_list = []
sorted_dict = {}

text = text.translate(str.maketrans("", "", string.punctuation)).lower()
text_list = text.split()
for i in text_list:
    new_dict[i] = new_dict.get(i, 0) + 1

sort = sorted(new_dict, key=new_dict.get, reverse=True)
for i in sort:
    sorted_dict[i] = new_dict[i]

count = 0
for key, value in sorted_dict.items():
    if count < 10:
        print(f"Слово '{key}', {value} раз")
        count += 1
