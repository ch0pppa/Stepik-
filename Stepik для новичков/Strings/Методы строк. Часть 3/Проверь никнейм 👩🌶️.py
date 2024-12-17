# Считываем ввод пользователя
nickname = input().strip()
# Изначально считаем, что никнейм некорректный
is_correct = "Incorrect"
# Проверяем условия для никнейма
if nickname.startswith('@') and 5 <= len(nickname) <= 15:
    # Проверяем, что все символы, кроме первого (@), являются строчными буквами или цифрами
    if all(char.islower() or char.isdigit() for char in nickname[1:]):
        is_correct = "Correct"
# Выводим результат проверки
print(is_correct)