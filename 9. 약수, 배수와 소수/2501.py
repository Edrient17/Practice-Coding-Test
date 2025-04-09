# 약수 구하기

N, K = map(int, input().split())

root = int(N ** 0.5)
li = []

for i in range(1, root + 1):
    if N % i == 0:
        li.append(i)
        if N // i != i:
            li.append(N // i)

li.sort()

if K > len(li):
    print(0)
else:
    print(li[K-1])
