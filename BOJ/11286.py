from queue import PriorityQueue
import sys
print = sys.stdout.write
myque = PriorityQueue()
input = sys.stdin.readline
n = int(input())

for i in range(n):
    request = int(input())
    if request == 0:
        if myque.empty():
            print('0\n')
        else:
            temp = myque.get()
            print(str(temp[1])+'\n')
    else:
        myque.put((abs(request), request))