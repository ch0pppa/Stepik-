count_fives = 0
while True:
  grade = int(input())
  if grade <= 0 or grade > 5:
    break
  if grade == 5:
    count_fives += 1

print(count_fives)

    