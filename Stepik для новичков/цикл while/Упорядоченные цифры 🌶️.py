num = int(input())
postoyannaya = num % 10
answer = 0
while num != 0:
    nepost = num % 10
    if postoyannaya <= nepost:
        answer = 'YES'
        num //= 10
        postoyannaya = nepost
    else:
        answer = 'NO'
        break
print(answer)