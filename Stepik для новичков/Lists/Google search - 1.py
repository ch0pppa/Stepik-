n = int(input())
lines = []
for i in range(n):
    lines.append(input())
query = input().lower()

for line in lines:
    if query in line.lower():
        print(line)
