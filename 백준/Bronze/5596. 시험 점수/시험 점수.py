Min = list(map(int, input().split()))
Man = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(0, 4):
    sum1 += Min[i]
for i in range(0, 4):
    sum2 += Man[i]

if sum1 > sum2:
    print(sum1)
elif sum1 < sum2:
    print(sum2)
else:
    print(sum1)

