number_input = input()
if number_input != 'Я':
    next_a = chr((ord(number_input))+1)
    print(next_a)
else:
    print('Дальше букв нет')