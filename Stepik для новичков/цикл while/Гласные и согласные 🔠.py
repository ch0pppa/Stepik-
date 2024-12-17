s = input()
vowel = "ауоыиэяюе"
consonant = "бвгджзйклмнпрстфхцчшщ"
count_vowel = 0
count_consonant = 0
for char in s:
    if char.lower() in vowel:
        count_vowel += 1
    elif char.lower() in consonant:
        count_consonant += 1
print('Количество гласных букв равно', count_vowel)
print('Количество согласных букв равно', count_consonant)