# Задача 6

# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билет

# 385916 -> yes
# 123456 -> no

print('Введите шестизначное число: ')
n = int(input())
res1 = n // 100000 + (n // 10000) % 10 + (n // 1000) % 10
res2 = (n // 100) % 10 + (n // 10) % 10 + n % 10

if res1 == res2:
    print('Yes')
else:
    print('No')
