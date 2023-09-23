# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def rich_limit():
    global s
    if s >= RICHLIMIT:
        s *= RICHTAX


def three_operation():
    global s
    global count
    if count % THREEOPERATIONS == 0 and count != 0:
        s *= BONUSTHREE
        count = 0


def refill():
    global new_list
    global s
    global count
    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        count += 1
        s += withdrow
        new_list.append(s)


def deregist():
    global new_list
    global s
    global count
    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        comission = withdrow * COMMISSIONOUTDROW
        if comission < MINLIMIT:
            comission = MINLIMIT
        elif comission > MAXLIMIT:
            comission = MAXLIMIT
        if (comission + withdrow) < s:
            s -= (withdrow + comission)
            count += 1
            new_list.append(s)


def atm():
    global s
    global new_list
    while True:
        action = input('Введите операцию 1,2,3: ')
        rich_limit()
        three_operation()
        if action == '1':
            refill()
        elif action == '2':
            deregist()
        else:
            break
        print(s)
    print(new_list)


new_list = []
s = 10000
count = 1
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600

atm()
