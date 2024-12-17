word = ''
max = 0

for i in range(1, 5):
    words = input()
    summ = 0
    for j in words:
        summ += ord(j)
        if summ > max:
            max = summ
            word = words

print(word)
