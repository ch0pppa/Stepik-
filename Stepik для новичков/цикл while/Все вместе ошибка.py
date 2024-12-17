n = int(input())
temp = n
#сумма цифр
SumDighit = 0
while temp>0:
    SumDighit+=temp%10
    temp//10
#колличество цифр в числе
CountDighit=0
while temp>0:   
    CountDighit+=1
    temp//10
#произведение цифр в числе
ProductDighit=1
while temp>0:
    ProductDighit*=temp%10
    temp//10
#среднее арифметическое 
AvarageDighit = SumDighit/CountDighit
#первая цифра числа
while temp>=10:
    FirstDighit = temp//10
#последняя цифра числа
LastNumber = temp%10
#сумма первого и последнего числа 
SumFirstLast = FirstDighit + LastNumber

print(SumDighit)   
print(CountDighit)
print(ProductDighit)
print(AvarageDighit)
print(FirstDighit)
print(SumFirstLast)