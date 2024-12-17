n = int(input())

# Проверяем, что число больше 9
if n <= 9:
  print("YES")
else:
  # Получаем первую цифру
  first_digit = n % 10
  n //= 10

  # Проверяем остальные цифры
  same_digits = True
  while n > 0:
    if n % 10 != first_digit:
      same_digits = False
      break
    n //= 10

  # Выводим результат
  if same_digits:
    print("YES")
  else:
    print("NO")