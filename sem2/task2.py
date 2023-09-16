# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#  Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import math
import fractions

a = "20/30"
b = "4/7"

a1 = ""
a2 = ""
b1 = ""
b2 = ""

flag = True
for i in a:
    if i == "/":
        flag = False
    elif flag:
        a1 += i
    else:
        a2 += i
a1 = int(a1)
a2 = int(a2)

flag = True
for i in b:
    if i == "/":
        flag = False
    elif flag:
        b1 += i
    else:
        b2 += i
b1 = int(b1)
b2 = int(b2)

mult1 = a1*b1
mult2 = a2*b2
nod = math.gcd(mult1, mult2)
mult1 /= nod
mult2 /= nod
mult = str(int(mult1)) + "/" + str(int(mult2))
print(mult)

summa1 = a1*b2 + a2*b1
summa2 = a2*b2
nod = math.gcd(summa1, summa2)
summa1 /= nod
summa2 /= nod
summa = str(int(summa1)) + "/" + str(int(summa2))
print(summa)

f1 = fractions.Fraction(a1, a2)
f2 = fractions.Fraction(b1, b2)

if summa == str(f1+f2) and mult == str(f1*f2):
    print("все ок")
