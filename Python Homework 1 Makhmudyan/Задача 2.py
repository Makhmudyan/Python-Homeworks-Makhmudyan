# Задача 2

# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите число: ")
n = int(input())
res = 0
while n > 0:
    x = n % 10
    res += x
    n = n // 10
print (res)