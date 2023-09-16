# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное

#  строковое представление. Функцию hex используйте для проверки своего результата.


number = int(input("введите число: "))
result = ""
hex_result = hex(number)


while number > 0:
    if number % 16 < 10:
        result = str(number % 16) + result
    elif number % 16 == 10:
        result = "a"+result
    elif number % 16 == 11:
        result = "b"+result
    elif number % 16 == 12:
        result = "c"+result
    elif number % 16 == 13:
        result = "d"+result
    elif number % 16 == 14:
        result = "e"+result
    elif number % 16 == 15:
        result = "f"+result
    number //= 16

print(result)

if result == hex_result[2:]:
    print("все ок")