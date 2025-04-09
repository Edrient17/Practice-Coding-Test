# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

V -= A
count = (V // (A-B)) + 1
if (V % (A-B) != 0):
    count += 1

print(count)
