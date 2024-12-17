words= []
line = input()
while line != 'КОНЕЦ' and line != 'конец':
    words.append(line)
    line = input()

print(f"Минимальная строка ⬇️: {min(words)}")
print(f"Максимальная строка ⬆️: {max(words)}")
