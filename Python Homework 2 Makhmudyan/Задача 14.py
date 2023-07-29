# Задача 14

# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

N = int(input('N = '))
result = f"{N} -> "
for i in range(N):
    k = pow(2,i) 
    if k <= N:
        result += str(k) + ' ' 

print(result.strip())      




# n = int(input())
# result = f'{n} -> '
# i = 0
# while 2 ** i <= n:
#     print(2**i)
#     i += 1