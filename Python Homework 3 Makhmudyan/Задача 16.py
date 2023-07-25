#  Задача 16: 

#  Требуется вычислить, сколько раз встречается некоторое
#  число X в массиве A[1..N]. Пользователь в первой строке вводит
#  натуральное число N – количество элементов в массиве. В последующих
#  строках записаны N целых чисел A. Последняя строка содержит число X

#  5
#  1 2 3 4 5
#  3
#  -> 1


# N = int(input('N = '))
# list1 = []
# for i in range(N):
#     k = int(input())
#     list1.append(k)

# print(list1)
# count = 0
# X = int(input('X = '))
# for i in range(len(list1)):
#     if list1[i] == X:
#         count += 1

# print(count)



list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)