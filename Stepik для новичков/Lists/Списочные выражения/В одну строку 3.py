print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

'''
Для понимания обычный вариант
n = input().split()
num = []
for j in n:
    if int(j) % 2 == 0:
        s = int(j) ** 2
        if s % 10 != 4:
            num.append(s)
print(*num)
'''