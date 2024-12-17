# Считываем ввод пользователя
license_plate = input()
# Изначально считаем, что номер некорректный
is_valid = 'NO'
# Допустимые буквы для автомобильного номера
allowed_letters = 'АВЕКМНОРСТУХ'
# Проверяем, что длина строки соответствует одному из допустимых форматов
if 9 <= len(license_plate) <= 10:
    # Извлекаем буквы и цифры из номера
    letters_part = license_plate[0] + license_plate[4:6]
    digits_part = license_plate[1:4] + license_plate[7:]
    underscore_part = license_plate[6]
    # Проверяем, что цифры и символ подчеркивания на своих местах
    if digits_part.isdigit() and underscore_part == "_":
        is_valid = 'YES'
    # Проверяем, что все буквы являются допустимыми
    for char in letters_part:
        if char not in allowed_letters:
            is_valid = 'NO'
# Выводим результат проверки
print(is_valid)