# Задача 10

# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# n = int(input('n = '))
# count = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count += 1
        
# print(count if count < n/2 else n - count)


n = int(input())
count_o = 0
count_r = 0
for i in range(n):
    x = int(input())
    if x == 1:
        count_o += 1
    else:
        count_r += 1

# if count_o < count_r:
#     print(count_o)
# else:
#     print(count_r)

print(count_o if count_o < count_r else count_r)