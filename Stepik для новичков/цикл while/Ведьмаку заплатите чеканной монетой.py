money = int(input())
counter = 0
while money!=0:
    if money>=25:
        money-=25
        counter+=1
    elif money>=10:
        money-=10
        counter+=1
    elif money>=5:
        money-=5
        counter+=1
    elif money>=1:
        money-=1
        counter+=1
print(counter)
