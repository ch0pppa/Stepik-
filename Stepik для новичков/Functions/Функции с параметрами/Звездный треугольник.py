# Определение функции draw_triangle()
def draw_triangle(fill, base):
    # Верхняя половина треугольника
    for i in range(base // 2):
        print(fill * (i + 1))
    # Нижняя половина треугольника
    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))
# Считывание данных
fill = input()       # Запрос символа для заполнения треугольника
base = int(input())  # Запрос размера основания треугольника
# Вызов функции draw_triangle() для рисования треугольника
draw_triangle(fill, base)