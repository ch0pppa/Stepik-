# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# count = 0
# while True:
#     word = input()
#     if word == "стоп" or word == "хватит" or word == "достаточно":
#         break
#     else:
#         count += 1
# print(count)

# num = int(input())
# words = []
# while True:
    
# n = int(input())
# while n%7==0:
#   print(n)
#   n = int(input())

# sum = 0
# while True:
#   number = int(input())
#   if number < 0:
#     break
#   sum += number

# print(sum)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1

#     num = num // 10

# print(total)

# n = int(input())

# max_digit = 0
# min_digit = 9

# while n > 0:
#   digit = n % 10
#   if digit > max_digit:
#     max_digit = digit
#   if digit < min_digit:
#     min_digit = digit
#   n //= 10

# print("Максимальная цифра равна",max_digit)
# print("Минимальная цифра равна", min_digit)

# n = int(input())

# # Проверяем, что число больше 9
# if n <= 9:
#   print("Число должно быть больше 9")
# else:
#   # Сдвигаем цифры влево, пока не останется две
#   while n > 99:
#     n //= 10

#   # Теперь n содержит две последние цифры
#   second_digit = n % 10 
#   print(second_digit)


