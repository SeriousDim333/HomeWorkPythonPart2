# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать
# числа из вашего билета из list1 со списком выпавших чисел list2
# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]


class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        count = 0
        new_list = []
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    count += 1
                    new_list.append(i)
                    break
        if new_list:
            print(
                f'Совпадающие числа: {new_list} \nКоличество совпадающих чисел: {count}')
        else:
            print("Совпадающих чисел нет.")


list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

# class LotteryGame:
#     def __init__(self, list1, list2):
#         self.list1 = list1
#         self.list2 = list2

#     def compare_lists(self):
#         matching_numbers = []  # Инициализируем список для совпадающих чисел

#         for num1 in self.list1:
#             if num1 in self.list2:
#                 matching_numbers.append(num1)
#         if matching_numbers:
#             print("Совпадающие числа:", matching_numbers)
#             print("Количество совпадающих чисел:", len(matching_numbers))
#         else:
#             print("Совпадающих чисел нет.")

#         return matching_numbers
