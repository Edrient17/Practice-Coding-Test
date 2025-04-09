# 벌집

N = int(input())

d = 6
count = 0
while(N > 0):
    if count == 0:
        N -= 1
    else:
        N -= d
        d += 6
    
    count += 1

print(count)