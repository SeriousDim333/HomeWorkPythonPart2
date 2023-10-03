# Создайте функцию генератор чисел Фибоначчи fibonacci.
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8


# def fibonacci():
#     fib1 = 0
#     fib2 = 1
#     while True:
#         yield fib1
#         fib_sum = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib_sum

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
for i in range(10):
    print(next(f))