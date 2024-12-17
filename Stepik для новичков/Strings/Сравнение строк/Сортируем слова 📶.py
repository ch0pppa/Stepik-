word1 = input()
word2 = input()
word3 = input()

# Сортируем слова в лексикографическом порядке
words = sorted([word1, word2, word3])

# Выводим отсортированные слова на одной строке
print(" ".join(words))