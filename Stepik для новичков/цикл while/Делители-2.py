n = int(input())
for i in range(1, n+1):        # циклом перебираем все числа от 1 до n включительно
    print(i, end = '')         # вывод текущего числа
    for j in range(1, i+1):    # цикл поиска делителя 
        if i % j == 0:         # если число делится без остатка
            print('+', end='') # то печатаем + без пробела
    print()                    # переход на новую строку