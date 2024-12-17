string = input().split()
new_string = [int(i)**3 for i in string]
print(*new_string)
