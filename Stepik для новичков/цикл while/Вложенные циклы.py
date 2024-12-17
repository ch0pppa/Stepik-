# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# number = int(input())
# for i in range (number):
#     print("")
#     for j in range (3):
#         print(number,end="")

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()

# n = int(input())
# for i in range (1,n+1):
#     print(" ")
#     for j in range (1,10):
#         print(i,"+",j,"=", i+j)

    
# n = int(input())
# # Находим середину пирамиды
# centr = n // 2 + 1
# # Инициализируем счетчик звездочек в строке
# count = 0
# # Проходим по строкам пирамиды от 1 до n
# for i in range(1, n + 1):
#     if i > centr:
#         count -= 1  # Если перешли за середину, уменьшаем количество звездочек
#     else:
#         count += 1  # В противном случае увеличиваем количество звездочек
    
#     # Выводим звездочки в строке
#     for _ in range(count):
#         print('*', end='')
#     # Переходим на новую строку для следующей строки пирамиды
#     print()

# n = int(input())
# # Внешний цикл для создания строк с числами от 1 до n
# for i in range(1, n + 1):
#     # Внутренний цикл для повторения числа i в строке i раз
#     for j in range(i):
#         print(i, end='')  # Выводим число i
#     print()  # Переходим на новую строку после каждой строки

#делители-2






