import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 1
end = max(height)

while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in height:
        temp = i-mid
        if temp > 0:
            tree += temp
    if m <= tree:
        start = mid+1
    else:
        end = mid -1
print(end)