# 소인수분해

N = int(input())
result_list= []

for i in range(2, int(N ** 0.5)+1):
    while N % i == 0:
        result_list.append(i)
        N = N // i

if N > 1:  # 남은 N이 소인수인 경우
    result_list.append(N)

for i in result_list:
    print(i)
