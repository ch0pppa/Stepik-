import random

def guess_the_number(lives):
    """
    Функция имитирует игру "Угадай число" с 5 попытками.

    :param lives: Целое число, представляющее количество жизней игрока (по умолчанию 5).
    :return: Ничего.
    """
    lives = 5
    # Генерируем случайное число.
    random_number = random.randrange(1, 100)

    # Основной цикл игры.
    for i in range(lives):

        # Запрашиваем ввод у пользователя.
        number = int(input("Введите число от 1 до 100: "))

        # Проверяем, угадано ли число.
        if number < random_number:
            print("Ваше число меньше загаданного.")
        elif number > random_number:
            print("Ваше число больше загаданного.")
        else:
            print("Вы угадали!")
            return

# Если попытки закончились, выводим сообщение о поражении.
    print("Вы проиграли. Загаданное число было", random_number)



