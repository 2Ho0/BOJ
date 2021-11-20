"""import sys
n = int(input())
card1 = list(map(int, sys.stdin.readline().split()))
card1.sort()
m = int(input())
card2 = list(map(int, sys.stdin.readline().split()))

for i in card2:
    count=0
    start = 0
    end = len(card1)-1

    while start<=end:
        mid = (start+end)//2
                   
        if card1[mid]==i:
            count+=1
            if mid==len(card1)-1:
                break
            if card1[mid]==card1[mid-1]:
                end = mid-1
                continue
            if card1[mid]==card1[mid+1]:
                start=mid+1
                continue
            
            else:
                break
        elif card1[mid]<i:
            start=mid+1
        else:
            end = mid-1
    print(count, end=' ')"""
"""import sys
n = int(input())
card1 = list(map(int, sys.stdin.readline().split()))
card1.sort()
m = int(input())
card2 = list(map(int, sys.stdin.readline().split()))

for i in card2:
    c = card1.count(i)
    print(c, end=" ")"""
n,L,k,M = int(input()),list(map(int, input().split())),int(input()),list(map(int, input().split()))
d = []
L.sort()
def upper_bound(s, e, d):
    while(e - s > 0):
        m = (s+e)//2
        if(L[m] <= d):
            s = m+1
        else:
            e = m
    return e
    
def lower_bound(s, e, d):
    while(e - s > 0):
        m = (s+e)//2
        if(L[m] < d):
            s = m+1
        else:
            e = m
    return e
    
for i in M:
    d.append(upper_bound(0, n, i) - lower_bound(0, n, i))
print(d)