s=input()              # Получаем строку
c=0                    # Переменная для кол-ва символов
a=''                   # Переменная для подсчета самого частого символа
for i in s:            # Проверяем посимвольно
    if s.count(i)>=c:  # Если количество символов в строке больше либо равны уже сохраненому
        c=s.count(i)   # Записываем новое значение кол-ва символов
        a=i            # Запоминаем символ
print(a)