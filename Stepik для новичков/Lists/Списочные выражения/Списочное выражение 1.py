n = int(input())
numbers = [i**2 for i in range (1,n+1)]
print(*numbers, sep = "\n")