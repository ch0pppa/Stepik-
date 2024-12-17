string1 = input().lower()
string2 = input().lower()

string1 = ''.join(char for char in string1 if char.isalpha())
string2 = ''.join(char for char in string2 if char.isalpha())

if string1 == string2:
    print("YES")
else:
    print("NO")

