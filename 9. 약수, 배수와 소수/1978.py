# 소수 찾기

A = 1000
li = [i for i in range(2, A + 1)]
prime = []

while(len(li) != 0):
    i = li[0]
    if i * i > A: # 더 이상 소수의 배수 제거는 필요 없음 → 남은 수는 모두 소수
        prime.extend(li) # 리스트 li 안에 있는 모든 값을 prime 리스트에 "한꺼번에" 추가
        break

    prime.append(i)
    li[:] = [num for num in li if num % i != 0] # [:]를 통해 기존 리스트 객체의 "내용"을 바꾼다.

N = int(input())
numbers = list(map(int, input().split()))

count = 0

for i in numbers:
    if i in prime:
        count += 1

print(count)
