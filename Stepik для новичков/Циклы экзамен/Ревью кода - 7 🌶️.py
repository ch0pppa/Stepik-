n = int(input())
s = 0
while n > 0:
    number = n % 10
    if number % 2 == 0:
        s+=number
    n //= 10
print(s)