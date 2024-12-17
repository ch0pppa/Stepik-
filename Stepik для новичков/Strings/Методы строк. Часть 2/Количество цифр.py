string = input()
count = 0
for char in range(10):
    count += string.count(str(char))
print(count)