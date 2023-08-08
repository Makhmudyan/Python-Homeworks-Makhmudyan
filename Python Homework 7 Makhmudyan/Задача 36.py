# Задача 36

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{k:>3}" for k in i])


print_operation_table(lambda x, y: x * y)



# -------------------------------------------------------------------------------


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print("   ", end='')  # Печатаем пустую ячейку в верхнем левом углу
    
#     # Печатаем заголовки столбцов
#     for col in range(1, num_columns + 1):
#         print(f"{col:4}", end='')
#     print()  # Переходим на новую строку
    
#     # Печатаем разделительную линию
#     print(" " + "-" * (4 * num_columns + 1))
    
#     # Печатаем строки таблицы
#     for row in range(1, num_rows + 1):
#         print(f"{row}|", end='')  # Номер строки
        
#         for col in range(1, num_columns + 1):
#             result = operation(row, col)  # Вычисляем результат для текущей ячейки
#             print(f"{result:4}", end='')  # Печатаем значение ячейки
            
#         print()  # Переходим на новую строку

# # Пример использования с операцией умножения
# print_operation_table(lambda x, y: x * y)
