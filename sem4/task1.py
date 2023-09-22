# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def trans_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix))


a = [[1, 2, 3], [4, 5, 6]]
print(trans_matrix(a))
