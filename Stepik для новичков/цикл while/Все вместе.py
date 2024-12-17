n = int(input())

# Сумма цифр
sum_of_digits = 0
temp = n
while temp > 0:
  sum_of_digits += temp % 10
  temp //= 10

# Количество цифр
count_of_digits = 0
temp = n
while temp > 0:
  count_of_digits += 1
  temp //= 10

# Произведение цифр
product_of_digits = 1
temp = n
while temp > 0:
  product_of_digits *= temp % 10
  temp //= 10

# Среднее арифметическое
average_of_digits = sum_of_digits / count_of_digits

# Первая цифра
first_digit = n
while first_digit >= 10:
  first_digit //= 10

# Последняя цифра
last_digit = n % 10

# Сумма первой и последней цифр
sum_of_first_and_last = first_digit + last_digit

# Вывод
print(sum_of_digits)
print(count_of_digits)
print(product_of_digits)
print(average_of_digits)
print(first_digit)
print(sum_of_first_and_last)