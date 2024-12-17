# class_number = int(input())
# correct_class = False

# for i in range(1, class_number + 1):
#     class_type = input()
#     if class_type[1].isdigit:
#         if '1' <= class_type[0] <= '9' and 'A' <= class_type[1] <= 'Z':
#             correct_class == True
#             print('YES')        
#     elif class_type[1].isalpha:
#         if class_type[0] == 1 and class_type[1] == 0:
#             if class_type[0] == 1 and class_type[1] == 1:
#                 if 'А' <= class_type[2] <= 'П':
#                     correct_class == True
#                     print('YES')

#     elif correct_class == False:
#         print('NO')


class_number = int(input())
correct_class = False

for i in range(1, class_number + 1):
    class_type = str(input())
    if len(class_type) == 2 and '0' <= class_type[0] <= '9' and 'А' <= class_type[-1] <= 'П':
        correct_class = True
        print('YES')

    else:
        correct_class = False
        print('NO')