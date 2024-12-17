# объявление функции
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Функция, которая проверяет, является ли число простым
def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num)):
        if num % i == 0:
            return False
        
    return True

# Функция, которая проверяет, является ли число четным
def is_even(num):
    return num % 2 == 0

def is_valid_password(password):
    l = password.split(":")
 # Проверяем, что пароль содержит три части
    if len(l) == 3:  
        l = [int(el) for el in l]   # Преобразуем каждую часть в целое число
        a, b, c = l[0], l[1], l[2]  # Присваиваем переменным значения из списка
        # Проверяем, что первая часть (a) является палиндромом, вторая часть (b) - простым числом,
        # а третья часть (c) - четным числом
        return is_palindrome(a) and is_prime(b) and is_even(c)
    return False  # Возвращаем False, если пароль не соответствует заданному формату

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))