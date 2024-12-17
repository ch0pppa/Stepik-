# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i

# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)


# n = int(input())

# for i in range(2, n+1):
#   if n % i == 0:
#     break
# print(i)

n = int(input())
for i in range (1,n+1):
  if 5<=i<=9 or 17<=i<=37 or 78<=i<=87 :
    continue
  print(i)
