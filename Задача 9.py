# Задача 9

# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# n = int(input('n = '))
# fact_res = 1
# i = 2
# while i <= n:
#     fact_res *= i
#     i+=1
# print(fact_res)



n = int(input('n = '))
fact_res_2 = 1
while n > 0:
   fact_res_2 *= n
   n -= 1
print(fact_res_2)