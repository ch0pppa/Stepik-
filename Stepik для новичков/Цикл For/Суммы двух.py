n = int(input())
numbers = []

# Ввод чисел в список
for i in range(n):
  numbers.append(int(input()))

# Создание списка сумм соседних чисел
sums = []
for i in range(n - 1):
  sums.append(numbers[i] + numbers[i + 1])

# Вывод списка сумм
print(sums)

        
