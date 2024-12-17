string = input()
english_letters = 'eyopaxcETOPAHXCBM'
russian_letters = 'еуорахсЕТОРАНХСВМ'
old_cost = 0
new_cost = 0

for i in string:
    old_cost += ord(i) * 3
    if i in english_letters:
        index = english_letters.index(i)
        russian_letter = russian_letters[index]
        new_cost += ord(russian_letter) * 3
    else:
        new_cost += ord(i) * 3

print(f"Старая стоимость: {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")