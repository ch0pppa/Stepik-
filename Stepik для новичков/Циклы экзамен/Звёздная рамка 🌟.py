# n = int(input())
# if 3 <= n <= 19: 
#     print("*"*19)
#     for i in range (n-2):
#         print("*"+" "*17+"*")
#     print("*"*19)

n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        cur_sep = "*"
    else:
        cur_sep = " "
        
    print("*", "*", sep=cur_sep * 17)