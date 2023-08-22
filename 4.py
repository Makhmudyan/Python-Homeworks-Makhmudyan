# from random import randint
# from time import time


# def list_gen(mi=-5, ma=5, le=10):
#  return [randint(mi, ma) for i in range(le)]


# # bubble_sort
# def algo_time(func, x):
#     start = time()
#     func(x)
#     finish = time() - start
# print(f'Выполнение за {finish} сек.')


# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst


# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
# pivot = lst[len(lst) // 2]
# left = list(filter(lambda x: x < pivot, lst))
# center = [i for i in lst if i == pivot]
# right = list(filter(lambda x: x > pivot, lst))
# return quick_sort(left) + center + quick_sort(right)


# def binary_search(lst, value, left, right):
#  if right < left:
#  return None
#  middle_point = (right - left) // 2 + left
#  if lst[middle_point] < value:
#  return binary_search(lst, value, middle_point + 1, right)
#  elif lst[middle_point] > value:
#  return binary_search(lst, value, left, middle_point - 1)
#  else:
#  return middle_point

# my_list = list_gen(-100, 100, 1_000_000)
# # algo_time(bubble_sort, my_list)
# # print(my_list)
# start = time()
# my_list.sort()
# finish = time() - start
# # print(my_list)
# print(f'Выполнение за {finish} сек.')

# print('-' * 50)

# my_list = list_gen(-10, 10, 20)
# # print(my_list)
# start2 = time()
# my_list_sorted = quick_sort(my_list)
# finish2 = time() - start
# print(my_list_sorted)
# print(f'Выполнение за {finish2} сек.')

# print('-' * 50)

# start3 = time()
# value_to_search = 0
# result_of_binary_search = binary_search(my_list_sorted, value_to_search, 0, len(my_list_sorted)-1)
# finish3 = time() - start
# # print(f'Иcкомое число {my_list_sorted} ')
# print(f'{result_of_binary_search}')
# print(f'Выполнение за {finish3} сек.')



# # Дополнительный код
# from random import randint
# import time

# def bubble(sp):
#  start = time.time()
#  for i in range(len(sp)-1):
#  for j in range(len(sp)-i-1):
#  if sp[j] > sp[j+1]:
#  sp[j], sp[j+1] = sp[j+1],sp[j]
#  print(sp)
#  print(time.time() - start)

# def counting_sort(sp):
#  start = time.time()
#  max_item=max(sp)
#  lst=[0 for _ in range(max_item+1)]
#  for i in sp:
#  lst[i]=lst[i]+1
#  print(lst)
#  index=0
#  # for i in range(len(lst)):
#  # for j in range(lst[i]):
#  # sp[index]=i
#  # index+=1
#  res_sp = []
#  for i in range(len(lst)):
#  if lst[i]:
#  res_sp.extend([i] * lst[i])
#  print(res_sp)
#  print(time.time() - start)

# print(sp := [randint(0, 10) for _ in range(20)])
# bubble(sp)
# counting_sort(sp)

# ----------------------------------------------------

# Необходимо написать алгоритм поиска всех доступных комбинаций 
# (посчитать количество) для количества кубиков К с количеством граней N. 
# У вас есть 2 варианта на выбор - количество кубиков может быть строго 
# ограничено (4 кубика, например), либо их количество будет динамическим. 
# Выбор за вами. Если вы реализуете простой вариант, обращает внимание, 
# что данное решение имеет сложность 0(n4), но если количество кубиков 
# сделать переменной, то она трансформируется в 0(nk) что будет представлять 
# собой экспоненциальную сложность. Для второго решения очевидно, 
# что его сложность 0(nk) с самого начала.

# import time
# import math

# n = int(input('Введите кол-во греней: '))
# k = int(input('Введите кол-во кубиков: '))

# def recomb(n,k):
#     start = time.time()
#     lst = [str(x) for x in range(1,n+1)]
#     for _ in range(1,k):
#       for _ in range(len(lst)):
#         item = lst.pop(0)
#         for i in range(n):
#             lst.append(item + str(i+1))
#     lst_set = set()
#     for item in lst:
#         item = ''.join(sorted(list(item)))
#         lst_set.add(item)
#     print(f'Результат: {len(lst_set)} Время: {time.time() - start}')
   
# def comb_form(n,k):
#    start = time.time()
#    res = int(math.factorial(n + k - 1) / (math.factorial(k) * math.factorial(n - 1)))
#    print(f'Результат: {res} Время: {time.time() - start}')

# recomb(n, k)
# comb_form(n, k)


# s = str()
# combos = set()

# def throw(k: int, output: str):
#     if k == 1:
#         for i in range(1, n + 1):
#             combos.add(int(''.join(sorted(output + str(i)))))
#     else:
#        for i in range(1, n + 1):
#             throw(k - 1, output + str(i))

# print(f'Всего {k} кубиков с {n} сторонами')
# start = time.time()
# throw(k, s)
# print(f'Количество уникальных комбинаций {len(combos)}')
# print(f'Время выполнения {time.time() - start} сек.')


#                 #   ----

# from random import randint
# import time

# def work_time(func, x):
#     start = time.time()
#     rez = func(x)
#     print(f'Числр отгадано и это {rez[0]} за {rez[1]} итераций')
#     print(f'Время ушло: {time.time() - start}')
#     print()

# def perebor(x):
#     for i in range(upper+1):
#         if i == x:
#             break
#     fin = time.time()
#     return (i, i)


# def random_guess(x):
#     k = 1
#     num = randint(0, upper)
#     while x != num:
#         num = randint(0, upper)
#         k +=1
#     return (num, k)


# def smart_random_guess(x):
#     k = 1
#     num = randint(0, upper)
#     s = {num}
#     while x != num:
#         while num in s:
#             num = randint(0, upper)
#         s.add(num)
#         k += 1
#     return (num, k)



# def from_list(x):
#     k = 0
#     sp =[x for x in range(upper+1)]
#     a = None
#     while a != x:
#         index = randint(0, len(sp) - 1)
#         a = sp.pop(index)
#         k += 1
#     return (a, k)


# def binary_search(x):
#     k = 1
#     left = 0
#     right = upper
#     current = round ( (right + left) / 2)
#     while current != x:
#         if current < x:
#             left = current + 1
#         else:
#             right = current - 1
#         current = round ( (right + left) / 2)
#         k += 1
#         # print(f"Left: {left} Right: {right} Current: {current} ")
#         # input()
#     return (current, k)

# upper = 10000

# x = randint(0,upper)
# sp = (perebor, random_guess, smart_random_guess, from_list, binary_search)
# for f in sp:
#     work_time(f, x)
# # random_guess(x)
# # smart_random_guess(x)
# # from_list(x)
# # binary_search(x)

# ----------------------------------------------------

# def calc_count(sp):
#     total = 0
#     for item in sp:
#         if str(type(item)) == "<class 'list'>":
#         # if isinstance(item, list):
#             total = total + calc_count(item)
#         else:
#             total += item
#     return total    

# count_angola = 18
# count_new_york = [20, [10, 7]]
# count_chicago = 15
# count_usa = [count_new_york, count_chicago]
# count_all = [count_angola, count_usa]
# print (count_all)
# print(type(count_all))
# print(calc_count(count_all))

# ----------------------------------------------------

# Необходимо написать один из простых алгоритмов сортировки,
# имеющий сложность O(n2). 
# Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором. 
# Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них.


# from random import randint
# from time import time

# def list_gen(min = -5, max = 5, len = 5):
#     return[randint(min, max) for i in range(len)]

# my_list = list_gen()
# print(my_list)
# print()

# # bubble_sort
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#                 # print(lst)
#     return lst


# def algo_time(func, x):
#     start = time()
#     func(x)
#     finish = time() - start
#     print(f'Выподнение за {finish} сек.')


# print(bubble_sort(my_list))
# print()
# algo_time(bubble_sort, my_list)
# print()

# ----------------------------------------------------

# Написать алгоритм быстрого поиска (quicksort). 
# Пишем тесты для сравнения производительности сортировки больших массивов. 
# Для наглядного результата стоит сравнивать массивы до 100 000 элементов.
# При таком подходе будет явно видно, какая из сортировок окажется быстрее.

# from random import randint
# from time import time

# def list_gen(min = -100, max = 100, len = 1000000):
#     return[randint(min, max) for i in range(len)]

# my_list = list_gen()
# # print(my_list)

# def algo_time(func, x):
#     start = time()
#     func(x)
#     finish = time() - start
#     print(f'Выподнение за {finish} сек.')

# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst) // 2]
#     left = list(filter(lambda x: x < pivot, lst))
#     center = [i for i in lst if i == pivot]
#     right = list(filter(lambda x: x > pivot, lst))
#     return quick_sort(left) + center + quick_sort(right)
    


# # print(quick_sort(my_list))
# # print()
# algo_time(quick_sort,my_list)
# # print()
# # start = time()
# # my_list_sorted = quick_sort(my_list)
# # finish = time() - start
# # print(f'Выполнение за {finish} сек.')


# print('-'*50)
# my_list_2 = list_gen(-100, 100, 1000000)
# # print(my_list_2)
# start2 = time()
# my_list_2.sort()
# finish2 = time() - start2
# # print(my_list_2)
# print(f'Выполнение за {finish2} сек.')

# ----------------------------------------------------

# После успешной сортировки массива на нем можно использовать бинарный
# поиск. Необходимо реализовать алгоритм бинарного поиска по
# элементам.
# Стоит акцентировать внимание, что т.к. алгоритм использует подход
# «разделяй и властвуй», его удобно писать с помощью рекурсии.
# Так что стоит акцентировать внимание на алгоритмическую сложность
# данного алгоритма, что его выполнение многократно быстрее простого
# перебора на больших массивах

# from random import randint
# from time import time


# def list_gen(min = -10, max = 10, len = 20):
#     return[randint(min, max) for i in range(len)]

# def binary_search(lst, value, left, right):
#     if right < left:
#         return None
#     index = (right - left) // 2 + left
#     if lst[index] < value:
#         return binary_search(lst, value, index + 1, right)
#     elif lst[index] > value:
#         return binary_search(lst, value, left, index - 1)
#     else:
#         return index

# my_list = list_gen()
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.sort()
# start = time()
# value_to_search = 0
# result_of_binary_search = binary_search(my_list, value_to_search, 0, len(my_list)-1)
# finish = time() - start
# print(f'{result_of_binary_search}')
# print(f'Выполнение за {round(finish)} сек.')

# ----------------------------------------------------

# from random import randint
# from time import time


# # Генерация списка
# def list_gen(min_value=-5, max_value=5, lst_len=10):
#     return [randint(min_value, max_value) for i in range(lst_len)]


# # Текстовый разделитель
# def text_separator(message='', line_len=60):
#     part_line = int(line_len - len(message)) // 2 if int(line_len - len(message)) // 2 > 0 else 0
#     print(f"{'-' * part_line}{message}{'-' * part_line}")


# # Замер временных рамок
# def running_time(func, x):
#     starting = time()
#     returned_value = func(x)
#     duration = time() - starting
#     print(f'Выполнение за {duration} сек.')
#     if returned_value is not None:
#         return returned_value


# # Алгоритм: Сортировка пузырьком
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst


# # Алгоритм: Быстрая сортировка
# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     pivot = lst[len(lst) // 2]
#     left = list(filter(lambda x: x < pivot, lst))
#     center = [i for i in lst if i == pivot]
#     right = list(filter(lambda x: x > pivot, lst))
#     return quick_sort(left) + center + quick_sort(right)


# # Алгоритм: Быстрая сортировка (вариант из stack overflow)
# # https://stackoverflow.com/questions/18262306/quicksort-with-python
# def sort(array):
#     """Sort the array by using quicksort."""
#     less = []
#     equal = []
#     greater = []
#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         return sort(less)+equal+sort(greater)
#     else:
#         return array


# # Алгоритм: Сортировка подсчетом
# """ Не поддерживаются отрицательные значения """
# def counting_sort(sp):
#     max_item = max(sp)
#     lst = [0 for _ in range(max_item + 1)]
#     for i in sp:
#         lst[i] = lst[i] + 1
#     index = 0
#     # for i in range(len(lst)):
#     #     for j in range(lst[i]):
#     #         sp[index]=i
#     #         index+=1
#     # Ушли от двух вложенных циклов следующим кодом
#     res_sp = []
#     for i in range(len(lst)):
#         if lst[i]:
#             res_sp.extend([i] * lst[i])
#     return res_sp


# # Алгоритм: Бинарный поиск (вариант с рекурсией, на вход требуется заранее отсортированный список)
# def binary_search_rec(lst, value, left, right):
#     if right < left:
#         return None
#     middle_point = (right - left) // 2 + left
#     if lst[middle_point] < value:
#         return binary_search_rec(lst, value, middle_point + 1, right)
#     elif lst[middle_point] > value:
#         return binary_search_rec(lst, value, left, middle_point - 1)
#     else:
#         return middle_point


# # Алгоритм: Бинарный поиск (вариант без рекурсии, на вход требуется заранее отсортированный список)
# def binary_search(in_list: list, value: int):
#     left = 0
#     right = len(in_list) - 1
#     current = (right + left) // 2
#     while in_list[current] != value:
#         if right < left:
#             return None
#         if in_list[current] < value:
#             left = current + 1
#         else:
#             right = current - 1
#         current = (right + left) // 2
#     return current


# # Тестирование алгоритмов
# text_separator(' Сортировка пузырьком ')
# my_list = list_gen(1, 10, 10_000)
# print(my_list) if len(my_list) <= 20 else print(f'Кол-во элементов {len(my_list):,}')
# running_time(bubble_sort, my_list)
# print(my_list) if len(my_list) <= 20 else None

# text_separator(' Быстрая сортировка ')
# my_list = list_gen(-100_000, 100_000, 1_000_000)
# print(my_list) if len(my_list) <= 20 else print(f'Кол-во элементов {len(my_list):,}')
# my_list_sorted = running_time(quick_sort, my_list)
# print(my_list_sorted) if len(my_list_sorted) <= 20 else None

# text_separator(' Быстрая сортировка (вариант из stack overflow) ')
# my_list = list_gen(-100_000, 100_000, 1_000_000)
# print(my_list) if len(my_list) <= 20 else print(f'Кол-во элементов {len(my_list):,}')
# my_list_sorted = running_time(sort, my_list)
# print(my_list_sorted) if len(my_list_sorted) <= 20 else None

# text_separator(' Встроенная сортировка Python ')
# my_list = list_gen(-100_000, 100_000, 1_000_000)
# print(my_list) if len(my_list) <= 20 else print(f'Кол-во элементов {len(my_list):,}')
# my_list_sorted = running_time(sorted, my_list)
# print(my_list_sorted) if len(my_list_sorted) <= 20 else None

# text_separator(' Сортировка подсчетом ')
# sp = list_gen(1, 200_000, 1_000_000)
# print(sp) if len(sp) <= 20 else print(f'Кол-во элементов {len(sp):,}')
# sp2 = running_time(counting_sort, sp)
# print(sp2) if len(sp2) <= 20 else None

# text_separator(' Бинарный поиск (с рекурсией) ')
# value_to_search = 0  # Искомое число
# print(my_list_sorted) if len(my_list_sorted) <= 20 else print(f'Кол-во элементов {len(my_list_sorted):,}')
# starting = time()
# i = binary_search_rec(my_list_sorted, value_to_search, 0, len(my_list_sorted) - 1)
# duration = time() - starting
# print(f'Искомое число {my_list_sorted[i]} найдено по индексу {[i]}.') if i else print('Искомое число не найдено.')
# print(f'Выполнение за {duration} сек.')

# text_separator(' Бинарный поиск (без рекурсии) ')
# value_to_search = 0  # Искомое число
# print(my_list_sorted) if len(my_list_sorted) <= 20 else print(f'Кол-во элементов {len(my_list_sorted):,}')
# starting = time()
# i = binary_search(my_list_sorted, value_to_search)
# duration = time() - starting
# print(f'Искомое число {my_list_sorted[i]} найдено по индексу {[i]}.') if i else print('Искомое число не найдено.')
# print(f'Выполнение за {duration} сек.')

# ----------------------------------------------------