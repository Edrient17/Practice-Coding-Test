# 중앙 이동 알고리즘

N = int(input())

p = 2
a = 1

for i in range(N):
    p += a
    a = a*2

print(p*p)