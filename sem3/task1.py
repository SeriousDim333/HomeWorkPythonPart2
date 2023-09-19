
#     Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]
new_list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8]
double_list = []

for i in new_list:
    if i in double_list:
        continue
    elif new_list.count(i) == 2:
        double_list.append(i)
print(double_list)
