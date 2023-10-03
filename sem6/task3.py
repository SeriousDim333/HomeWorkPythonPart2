# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая
# расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

from random import randint


def check_queens(queens):
    for i in queens:
        for j in queens:
            if i[0] == j[0] and i[1] == j[1]:
                continue
            elif abs(i[0]-j[0]) == abs(i[1]-j[1]) or i[0] == j[0] or i[1] == j[1]:
                return False
    else:
        return True


# def generate_boards():
#     board_list = []
#     while len(board_list) < 4:
#         one_board = []
#         while len(one_board) < 8:
#             ferz = ((randint(1, 8), randint(1, 8)))
#             if ferz not in one_board:
#                 one_board.append(ferz)
#         if check_queens(one_board):
#             board_list.append(one_board)
#     return board_list

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        one_board = []
        rnd_check = []
        while len(one_board) < 8:
            for i in range(1, 9):
                while len(one_board) < i:
                    rnd = randint(1, 8)
                    if rnd not in rnd_check:
                        ferz = (i, rnd)
                        one_board.append(ferz)
                        rnd_check.append(rnd)
        if check_queens(one_board):
            board_list.append(one_board)
    return board_list


print(generate_boards())
