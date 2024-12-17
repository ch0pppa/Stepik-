n = int(input())
decimal = []
for i in range (1,n+1):
    if n%i == 0:
        decimal.append(i)
print(decimal)

