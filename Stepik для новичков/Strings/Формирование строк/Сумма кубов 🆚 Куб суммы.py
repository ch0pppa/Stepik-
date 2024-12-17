a = int(input())
b = int(input())
sum_of_cubes = pow(a, 3) + pow(b, 3)
cube_of_sum = pow(a+b, 3)

result = f"Для чисел {a} и {b}:\n  Сумма кубов: {a}**3 + {b}**3 = {sum_of_cubes}\n  Куб суммы: ({a} + {b})**3 = {cube_of_sum}"
print(result)