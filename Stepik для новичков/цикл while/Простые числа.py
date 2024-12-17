a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:                # 1 не является простым числом
        continue              # пропускаем цикл
    for j in range(2, i):     # перебираем делители от 2 до i  
        if i % j == 0:        # если делится без остатка, то оно не простое
            break             # завершаем вложенный цикл
    else:
        print(i)
