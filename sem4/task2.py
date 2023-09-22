# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def reverse_kwargs(*, rev, acc, stroka):
    result = {}
    loc_dict = locals()
    del loc_dict["result"]
    print(loc_dict)
    for key, values in loc_dict.items():
        if isinstance(values, (dict, set, list)):
            result[str(values)] = key
        else:
            result[values] = key
    print(result)


reverse_kwargs(rev=True, acc="YES", stroka=4)

