# 소수

A = 10000
li = [i for i in range (2, A + 1)]
prime= []

while(len(li) != 0):
    i = li[0]

    if i * i > A:
        prime.extend(li)
        break

    prime.append(i)
    li[:] = [num for num in li if num % i != 0]

M = int(input())
N = int(input())

result_list = [i for i in prime if i >= M and i <= N]

if sum(result_list) != 0:
    print(sum(result_list))
    print(result_list[0])

else:
    print(-1)
