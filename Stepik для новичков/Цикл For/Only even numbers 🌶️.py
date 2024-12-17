numbers = []
for i in range(10):
    numbers.append(int(input()))
all_even = True
for number in numbers:
    if number%2!=0:
        all_even = False
    break
if all_even:
    print("YES")
else:
    print("NO")

    