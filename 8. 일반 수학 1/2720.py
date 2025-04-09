# 세탁소 사장 동혁

T = int(input())
li = [[0]*4 for _ in range(T)] # 0으로 채워진 T x 4 행렬 생성성

for i in range(T):
    C = int(input())
    li[i][0] = C // 25

    C = C % 25
    li[i][1] = C // 10

    C = C % 10
    li[i][2] = C // 5

    C = C % 5
    li [i][3] = C

for i in range(T):
    print(li[i][0], li[i][1], li[i][2], li[i][3])