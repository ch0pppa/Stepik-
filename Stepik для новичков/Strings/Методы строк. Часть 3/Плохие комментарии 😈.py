number = int(input())
for i in range (1,number+1):
    string = str(input())
    if string.isspace() or len(string) == 0:
         # 5. принт (переменную цикла, двоеточие и пробел перед COMMENT SHOULD BE DELETED)
        print(i, ": COMMENT SHOULD BE DELETED", sep='')
    else:
            # 6. иначе принт (переменная цикла, двоеточие, пробел, переменная s)
        print(i, ": ", string, sep='')