n = int(input())

if n==1:
    print("1")
elif n>1:    
# Инициализируем первые два числа Фибоначчи
    a = 1
    b = 1

# Выводим первые два числа
    print(a, end=" ")
    print(b, end=" ")

# Выводим оставшиеся числа Фибоначчи
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c