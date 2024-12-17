def find_all(target, symbol):

    positions = []
    start = 0

    while True:
        position = target.find(symbol, start)   
        if position == -1:
            break
        positions.append(position)
        start = position + 1

    return positions
s = input()
char = input()

# вызываем функцию
print(find_all(s, char)) 