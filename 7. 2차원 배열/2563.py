n = int(input())
background = [(i, j) for i in range(1, 101) for j in range(1, 101)]
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    x, y = li[i][0] + 1, li[i][1] + 1
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            if (j, k) in background:
                background.remove((j, k))

print(10000 - len(background))
