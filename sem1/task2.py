# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

digit = int(input("введите число больше 1 и меньше 100 тыс: "))

UP_BOUND = 100000
CHECK_BOUND = digit//2+1

if 1 < digit < UP_BOUND:
    for i in range(2, CHECK_BOUND):
        if digit % i == 0:
            print("непростое")
            break
    else:
        print("простое")
else:
    print("неправильное число")