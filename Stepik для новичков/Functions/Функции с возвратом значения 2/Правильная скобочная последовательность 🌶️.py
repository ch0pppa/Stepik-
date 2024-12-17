# Функция, которая проверяет правильность скобочной последовательности
def is_correct_bracket(text):
    # Пока в строке есть подстрока '()', заменяем её на пустую строку
    while '()' in text:
        text = text.replace('()', '')  
    return not text  # Возвращаем True, если вся строка опустела, что означает правильную последовательность
# Считываем данные (строку со скобками)
txt = input()
# Вызываем функцию и выводим результат
print(is_correct_bracket(txt))