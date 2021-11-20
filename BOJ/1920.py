import sys
n = int(input())
word = list(map(int, sys.stdin.readline().split()))
m = int(input())
w = list(map(int, sys.stdin.readline().split()))

word.sort()


for i in w:
    start = 0
    end = len(word)-1 
    c=0
    while start<= end:
        mid = (start+end)//2
        if word[mid]==i:
            print(1)
            c=1
            break
        elif word[mid]<i:
            start = mid+1
        else:
            end = mid-1
    if c==0:
        print(0)