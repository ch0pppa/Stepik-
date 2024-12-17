# объявление функции
def draw_box():
    for i in range(1,15):
        if 2<= i <=13:
            print("*"+(" "*8)+"*")
        else:
            print("*"*10)
    pass

# основная программа
draw_box()  # вызов функции