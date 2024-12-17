n = int(input())
numbers = []
for num in range(1, n+1):
    numbers.append(int(input()))

numbers.remove(min(numbers))
numbers.remove(max(numbers))

for number in numbers:
    print(number)