n = int(input())

negatives = []
zeros = []
positives = []

for i in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)

for num in negatives:
    print(num)
for num in zeros:
    print(num)
for num in positives:
    print(num)