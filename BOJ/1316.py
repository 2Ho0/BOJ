n = int(input())
m=[]

count = 0

for i in range(n):
    m.append(input())
    
for i in range(n):
    temp = []
    k=0
    count+=1
    for j in m[i]:
        if j not in temp:
            temp.append(j)
            k+=1
        else:
            if temp[k-1]!=j:
                count-=1
                break
print(count)

