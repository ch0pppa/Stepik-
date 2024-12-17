n_str = input()
n = int(n_str)

count_3 = n_str.count('3')
last_digit = int(n_str[-1])
count_last_digit = n_str.count(str(last_digit))
count_even = 0
sum_greater_5 = 0
prod_greater_7 = 1
count_0_5 = 0

for digit in n_str:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        count_even += 1
    if digit_int > 5:
        sum_greater_5 += digit_int
    if digit_int > 7:
        prod_greater_7 *= digit_int
    if digit_int == 0 or digit_int == 5:
        count_0_5 += 1

if prod_greater_7 == 1 and len([digit for digit in n_str if int(digit) > 7]) == 0:
    pass  # если нет цифр больше 7, то prod_greater_7 остается 1.
elif prod_greater_7 == 1 and len([digit for digit in n_str if int(digit) > 7]) == 1:
    prod_greater_7 = int([digit for digit in n_str if int(digit) > 7][0])

print(count_3)
print(count_last_digit)
print(count_even)
print(sum_greater_5)
print(prod_greater_7)
print(count_0_5)