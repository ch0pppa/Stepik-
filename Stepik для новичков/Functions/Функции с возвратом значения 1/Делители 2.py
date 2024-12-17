# объявление функции
def get_factors(num):
    decimals = []
    for i in range (1, num):
        if num % i == 0:
            decimals.append(i)
    decimals.append(num)
    quntity = len(decimals)
    return quntity

# считываем данные
num = int(input())

# вызываем функцию
print(get_factors(num))