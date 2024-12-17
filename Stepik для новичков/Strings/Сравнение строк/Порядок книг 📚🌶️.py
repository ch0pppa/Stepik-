n = int(input())
books = []

for _ in range(n):
    author, book_title = input().split('", "')
    author_last_name = author.split(' ')[0]
    books.append((author_last_name, book_title))

# Сортировка книг по фамилии автора, а затем по названию
books.sort()

# Проверка правильности сортировки
is_sorted = True
for i in range(1, n):
    if books[i - 1][0] > books[i][0] or (books[i - 1][0] == books[i][0] and books[i - 1][1] > books[i][1]):
        is_sorted = False
        break

# Вывод результата
if is_sorted:
    print("YES")
else:
    print("NO")