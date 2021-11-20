s = list(map(str,input().split()))
result = []

for i in range(len(s)):
    temp = []
    for j in reversed(s[i]):
        if j=="/":
            break
        temp.append(j)
    
    original = temp[-1]+temp[1]+temp[0]
    result.append(original)
result.sort()
for i in range(len(result)-1):
    if result[i]!=result[i+1] or i==len(result)-2:
        num = result.count(result[i])
        if num==1:
            continue
        print(result[i], num, end=' ')

"""if original not in result:
        result.append([original])
        n+=1
    if original in result:
        count+=1
        result[n].append(count)
for i in range(len(result)):
    if result[i][1]==1:
        continue
    if result[i][1]!=1:
        print(result[i], end =", ")
"""
         