# 그룹 단어 체커

N = int(input())

count = 0

for i in range(N):
    word = input()
    li = [word[0]]
    flag = True
    
    for j in range(1, len(word)):
        if word[j] != word[j-1]:
            if word[j] not in li:
                li.append(word[j])
            else:
                flag = False
                break
    
    if flag:
        count += 1

print(count)            
    