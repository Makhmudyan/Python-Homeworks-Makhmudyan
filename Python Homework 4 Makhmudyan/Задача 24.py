# Задача 24

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

# n = int(input('n = '))
# list = []
# for i in range(n):
#     n1 = int(input())
#     list.append(n1)
# print(list)

import random
bush = int(input("Введите количество кустов: "))
berry = list(random.randint(0, 10) for i in range(bush))
# bush = 4
# berry = [1, 2, 3, 4]
result = []
i = 0
sum = 0

print(berry)

while (i < bush):
    if (i == bush - 1):
        sum = berry[i] + berry[i - 1] + berry[0]
        result.append(sum)
        result.sort()
    else:
        sum = berry[i] + berry[i - 1] + berry[i + 1]
        result.append(sum)
        result.sort()
    i += 1
print(result)
print(f"Mаксимальное число ягод за один заход: {result[-1]}")