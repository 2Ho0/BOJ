import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0

for k in range(n):
    find = a[k]
    i = 0
    j = n-1

    while i < j:
        sum = a[i] + a[j]
        if sum < find:
            i+=1
        elif sum > find:
            j-=1
        else:
            if i!=k and j!=k:
                count +=1
                break
            elif i==k:
                i+=1
            elif j==k:
                j-=1

print(count)