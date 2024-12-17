number = int(input())
while number > 0:
    digit = number % 10
    number//=10
print(digit)