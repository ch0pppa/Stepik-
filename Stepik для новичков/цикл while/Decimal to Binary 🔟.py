n = int(input())
binary = ""

while n > 0:
  remainder = n % 2
  binary = str(remainder) + binary
  n //= 2

print(binary)