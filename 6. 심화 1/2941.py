# 크로아티아 알파벳

def check(s):
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
            count += 1
            i += 2
        elif s[i:i+3] == 'dz=':
            count += 1
            i += 3
        else:
            count += 1
            i += 1
    return count

s = input()
print(check(s))