import math
# объявление функции
def get_circle(radius):
    C = 2 * math.pi * radius
    S = math.pi * radius ** 2
    return C,S
# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)