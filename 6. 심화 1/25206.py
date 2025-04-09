# 너의 평점은

def convert(line):
    d = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F': 0}
    for key in d:
        if key in line:
            return d[key]
    return 0
    
total = 0
m = 0
d = ['1.0', '2.0', '3.0', '4.0']

for _ in range(20):
    name, credit, grade = input().split()
    if not 'P' in grade:
        for v in d:
            if v in credit:
                total += float(v) * convert(grade)
                m += float(v)
                break

print(total / m)