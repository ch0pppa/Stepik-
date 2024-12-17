# n = int(input())

# # Инициализация переменной для хранения текущего числа
# number = 1

# # Цикл по строкам треугольника
# for i in range(1, n + 1):
#     # Цикл по числам в строке
#     for j in range(i):
#         # Печать текущего числа с пробелом
#         print(number, end=" ")
#         # Увеличение числа на 1
#         number += 1
#     # Переход на новую строку после каждой строки треугольника
#     print()

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()