# Определение функции print_fio()
def print_fio(name, surname, patronymic):
    # Создаем строку, состоящую из первых букв имени, фамилии и отчества, и переводим ее в верхний регистр
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    # Выводим полученные инициалы
    print(full_name)
# Считывание данных
name, surname, patronymic = input(), input(), input()
# Вызов функции print_fio() для вывода инициалов
print_fio(name, surname, patronymic)