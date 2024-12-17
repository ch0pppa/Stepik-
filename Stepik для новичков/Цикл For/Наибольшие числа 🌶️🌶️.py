n = int(input())

# Ввод чисел последовательности
numbers = []
for i in range(n):
    numbers.append(int(input()))

 # Нахождение наибольшего и второго наибольшего чисел
max_number = max(numbers)
numbers.remove(max_number)
second_max_number = max(numbers)

# Вывод результата
print(max_number)
print(second_max_number)



