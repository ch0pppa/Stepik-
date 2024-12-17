def valid_function(num):
    if num.isdigit():
        if 1 <= int(num) <= 100:
            return True 
        else:
            return 'А может быть все-таки введем целое число от 1 до 100?'
while True:
    num = input()
    print(valid_function(num))