import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in lan:
        temp = i//mid
        count += temp
    if count < n:
        end = mid-1
    else:
        start = mid+1

print(end)