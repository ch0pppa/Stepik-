# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c  # Вычисляем дискриминант
    
    # Вычисляем два корня уравнения
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    
    return min(x1, x2), max(x1, x2)  # Возвращаем корни в порядке возрастания
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

# # объявление функции
# def solve(a, b, c):
#     D = b * b - 4 * a * c
#     return sorted([(-b - D ** 0.5) / (2 * a), (-b + D ** 0.5) / (2 * a)])

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)