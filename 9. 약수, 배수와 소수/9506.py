# 약수들의 합

while(True):
    n = int(input())
    if n == -1:
        break

    root = int(n ** 0.5)
    li = [1]

    for i in range(2, root + 1):
        if n % i == 0:
            li.append(i)
            if(n / i != i):
                li.append(n//i)

    if n == sum(li):
        print(f'{n} = ', end='')
        li.sort()
        for i in range(len(li)):
            print(li[i], end='')
            if(i != len(li)-1):
                print(' + ',end='')
        print()
    else:
        print(f'{n} is NOT perfect.')
