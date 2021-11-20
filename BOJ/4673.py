n = []
num = 1

for i in range(10000):
    n.append(i+1)

for i in range(10001):
    if num<10 and num>0:
        temp = num+num
    if num>=10 and num<100:
        a = num%10
        b = num//10
        temp = num+a+b
    if num>=100 and num<1000: #999
        a = num%10 #9
        b = num//10 #99
        c = b%10 #9
        d = b//10 #9
        temp = num + a+c+d
    if num>=1000 and num<=10000: #9999
        a = num%10 #9
        b = num//10 #999
        c = b%10 #9
        d = b//10 #99
        e = d%10 #9
        f = d//10 #9
        temp = num+a+c+e+f
    if temp in n:
        n.remove(temp)
        num+=1
    else:
        num+=1
for i in range(len(n)):
    print(n[i])

