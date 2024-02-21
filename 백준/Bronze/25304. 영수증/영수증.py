X = int(input())
N = int(input())
sum1 = 0
X
for i in range(1,N+1):
    a, b = input().split() # 값 2개씩 받기
    sum1 += int(a) * int(b) # int형 변환
if  X == sum1: # 금액 일치
    print('Yes')
else: # 금액 불일치
    print('No')