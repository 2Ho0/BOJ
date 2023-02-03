import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

ingredient = list(map(int, input().split()))
ingredient.sort()
i = 0
j = n-1
count = 0

while i < j:
    sum = ingredient[i] + ingredient[j]
    if sum < m:
        i+=1
    elif sum > m:
        j-=1
    else:
        i+=1
        j-=1
        count+=1
print(count)