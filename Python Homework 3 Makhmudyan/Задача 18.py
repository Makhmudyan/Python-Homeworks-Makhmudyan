# Задача 18: 

# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5


# N = int(input('N = '))
# list1 = []
# for i in range(N):
#     k = int(input())
#     list1.append(k)
# X = int(input('X = '))
# print(list1)
# y = abs(X - list1[0])
# index = 0
# for i in range(1, len(list1)):
#     count = abs(X - list1[i])
#     if count < y:
#         y = count
#         index = i
# print(list1[index])



list_1 = [1, 2, 3, 4, 5]
k = 5
# min=abs(k-list_1[0])
# index=0
# for i in range(1, len(list_1)):
#     count=abs(k-list_1[i])
#     if count < min:
#         min=count
#         index=i
# print(list_1[index])


m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
