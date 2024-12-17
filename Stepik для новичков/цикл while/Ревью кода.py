# max_number = -pow(10,6)
# sum_number = 0
# for i in range(1,11):
#     x = int(input())
#     if x <0:
#         sum_number += x
#     if 0 > x > max_number:
#         max_number = x
# if sum_number<0:     
#     print(sum_number)
#     print(max_number)
# else:
#     print("NO")

# sum_numbers = 0
# for i in range(1, 8):
#     number = int(input())
#     if number % 2 == 0:
#         sum_numbers += number

# if sum_numbers == 0:
#     print("0")
# else:
#     print(sum_numbers)

number = int(input())
product = 1
while number > 0:
    digit = number % 10
    product *= digit
    number //= 10
print(product)