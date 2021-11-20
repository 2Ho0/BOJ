n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

map1 = []
for x in arr1:
    y = ""   
    while x>0:
        y=str(x%2)+y
        x//=2
    if len(y)<n:
        y = '0'+y
    map1.append(y)
map2 = []
for x in arr1:
    y = ""   
    while x>0:
        y=str(x%2)+y
        x//=2
    if len(y)<n:
        y = '0'+y
    map2.append(y)

