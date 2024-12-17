n = int(input())
numbers = []

# Ввод чисел
for i in range(n):
    numbers.append(int(input()))

# Вывод чисел
for number in numbers:
    print(number)

print()  # Пустая строка

# Вывод значений функции
for number in numbers:
    result = pow(number,2) + 2 * number + 1
    print(result)