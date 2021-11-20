from math import ceil
n = list(input())
num = []

for i in range(len(n)):
    n[i] = int(n[i])

for i in range(10):
    num.append(n.count(i))

if num.index(max(num))==6 or num.index(max(num))==9:
    print(ceil((num[6]+num[9])/2))
else:
    print(max(num))