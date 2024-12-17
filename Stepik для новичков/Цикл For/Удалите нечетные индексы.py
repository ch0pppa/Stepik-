n = int(input())
numbers = []

# Ввод чисел в список
for i in range(n):
    numbers.append(int(input()))

# Удаление элементов по нечетным индексам

del numbers[1::2]

# Вывод полученного списка
print(numbers)
