# n = int(input())

# for i in range(n):
#     if i == 0 or i == n-1:
#         cur_sep = "*"
#     else:
#         cur_sep = " "
        
#     print("*", "*", sep=cur_sep * 17)

# n = int(input())
# while n > 999:
#     n //= 10
    
# print(n % 10)

# n = int(input())
# count = 0
# count_last_digit = 0
# count_even_numbers = 0
# count_lessThen5 = 0
# count_moreThen7 = 0
# count_0_or_5 = 0
# while n>0:
#     digit = n % 10
#     n //= 10
#     count_last_digit += 1
#     if digit == 3:
#         count +=1
#         print(count)
#     print(count_last_digit)
#     if n % 2 == 0:
#         count_even_numbers+=1
#         print(count_even_numbers)
#     if digit > 5:
#         count_lessThen5 += 1
#         print(count_lessThen5)
#     if digit > 7:
#         count_moreThen7*=digit
#         print(count_moreThen7)
#     else:
#         print("1")
#     if digit == 0 or digit == 5:
#         count_0_or_5+=1
#         print(count_0_or_5)

n = int (input('Введите ограничение диапазона для\
\nнахождения чисел Рамануджана  :)'))
total = 0
for n in range(1, n):
    for k in range(1, n):
        for m in range(1, n):
          for t in range(1, n):
              if n**3 + k**3 == m**3 + t**3 and n!=t and k!=m and k!=t  and  n>k and m>t and n>m:
                n,k ==m, t
                total += 1
                print('n =', n, 'k =', k, 'm =', m, 't=',  t, '=',n **3 + k **3 )
print('Общее количество натуральных решений =', total)    





