n=input()
count = 0
m = []
temp = []

for i in n:
    m.append(i)

for i in range(len(m)):
    for j in range(i+1,len(m)+1):
        s = m[i:j]
        t = []
        count+=1
        for k in s:
            if k in t:
                count-=1
                break
            if k not in t:
                t.append(k)
        if s in temp:
            count-=1
        if s not in temp:
            temp.append(s)
print(count)