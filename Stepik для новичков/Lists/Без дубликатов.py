n = int(input())
numbres = []
for i in range (n):
    number = input()
    if number not in numbres:
        numbres.append(number)
        print(number)