# объявление функции
def get_factors(num):
    decimals = []
    for i in range (1, num):
        if num % i == 0:
            decimals.append(i)
    decimals.append(num)
    return decimals

# считываем данные
num = int(input())

# вызываем функцию
print(get_factors(num))