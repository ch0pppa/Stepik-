def is_valid_triangle(side1, side2, side3):
    # Создаём отсортированный список из сторон
    s_list = sorted([side1, side2, side3])  
    # Проверяем, является ли сумма минимальной и средней сторон больше максимальной
    return s_list[0] + s_list[1] > s_list[2]
# Считываем длины сторон треугольника
a, b, c = int(input()), int(input()), int(input())
# Вызываем функцию и выводим результат
print(is_valid_triangle(a, b, c))