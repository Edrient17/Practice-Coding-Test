# 분수찾기

X = int(input())

r = 1
i = 0

while (X > 0):
    X -= r
    r += 1
    i += 1

if (i % 2 != 0):
    print(f'{-X + 1}/{X + i}')
else:
    print(f'{X + i}/{-X + 1}')
