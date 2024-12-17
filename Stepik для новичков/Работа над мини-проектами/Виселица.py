import random
def hangman(lives):
    """
    Функция имитирует игру "Виселица".

    :param lives: Целое число, представляющее количество жизней игрока.
    :return: Ничего.
    """

    # Список возможных слов.
    words = ["apple", "banana", "cherry", "dog", "elephant"]

    # Выбираем случайное слово.
    word = random.choice(words)

    # Список угаданных букв.
    guessed_letters = []

    # Основной цикл игры.
    while lives > 0 and word not in guessed_letters:

        # Выводим состояние игры.
        print("Осталось жизней:", lives)
        print("Угаданные буквы:", guessed_letters)

        # Запрашиваем ввод у пользователя.
        letter = input("Введите букву: ").lower()

        # Проверяем, угадана ли буква.
        if letter in word:
            # Добавляем букву в список угаданных.
            guessed_letters.append(letter)

            # Проверяем, угадали ли слово целиком.
            if set(guessed_letters) == set(word):
                print("Вы выиграли!")
                return
        else:
            # Отнимаем жизнь.
            lives -= 1

    # Если жизни закончились, выводим сообщение о поражении.
    if lives == 0:
        print("Вы проиграли.")