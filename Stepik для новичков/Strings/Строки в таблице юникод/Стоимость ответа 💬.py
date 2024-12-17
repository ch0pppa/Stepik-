string = input()
english_letters = 'eyopaxcETOPAHXCBM'
russian_letters = 'еуорахсЕТОРАНХСВМ'
old_cost = 0
new_cost = 0
for i in string:
    old_cost += ord(i)*3
    for j in english_letters:
        if i==j:
            new_cost += (ord(i)+ord (j))*3
        else:
            break
    for j in russian_letters:
        if i==j:
            new_cost += (ord(i)+ord (j))*3
        else:
            continue
print(f"Старая стоимость {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")