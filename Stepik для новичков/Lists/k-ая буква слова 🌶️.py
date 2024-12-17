n = int(input())
lists = []
for i in range (1, n+1):
    lists.append(input())
k = int(input())
result = ""
for list in lists:
    if len(list) >= k:
        result += list[k - 1]

print(result)

