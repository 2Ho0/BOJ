from collections import  deque 
gear1 = input()
gear1 = deque(gear1)
gear2 = input()
gear2 = deque(gear2)
gear3 = input()
gear3 = deque(gear3)
gear4 = input()
gear4 = deque(gear4)

m = []
k = int(input())
sum = 0
for i in range(k):
    m.append(list(map(int, input().split())))

def c(gear):
    gear.appendleft(gear[7])
    gear.pop()
def rc(gear):
    gear.append(gear[0])
    gear.popleft()
    

for i in range(k):
    if m[i][0]==1:
        if gear1[2]!=gear2[6]:
            if m[i][1]==1:
                c(gear1)
                if gear2[2]!=gear3[6]:
                    if gear3[2]!=gear4[6]:
                        rc(gear4)
                    c(gear3)
                rc(gear2)

            if m[i][1]==-1:
                rc(gear1)
                if gear2[2]!=gear3[6]:
                    if gear3[2]!=gear4[6]:
                        c(gear4)
                    rc(gear3)
                c(gear2)
        elif gear1[2]==gear2[6]:
            if m[i][1]==1:
                c(gear1)  
            if m[i][1]==-1:
                rc(gear1) 
    if m[i][0]==2:
        if gear2[2]!=gear3[6]:
            if m[i][1]==1:
                if gear3[2]!=gear4[6]:
                    c(gear4)
                if gear1[2]!=gear2[6]:
                    rc(gear1)
                c(gear2)
                rc(gear3)
    
            if m[i][1]==-1:
                if gear3[2]!=gear4[6]:
                    rc(gear4)
                if gear1[2]!=gear2[6]:
                    c(gear1)
                rc(gear2)
                c(gear3)
        elif gear2[2]==gear3[6]:
            if m[i][1]==1:
                if gear1[2]!=gear2[6]:
                    rc(gear1)
                c(gear2)
            if m[i][1]==-1:
                if gear1[2]!=gear2[6]:
                    c(gear1)
                rc(gear2)
    if m[i][0]==3:
        if gear2[2]!=gear3[6]:
            if m[i][1]==1:
                if gear1[2]!=gear2[6]:
                    c(gear1)
                if gear3[2]!=gear4[6]:
                    rc(gear4)
                c(gear3)
                rc(gear2)
                
            if m[i][1]==-1:
                if gear1[2]!=gear2[6]:
                    rc(gear1)
                if gear3[2]!=gear4[6]:
                    c(gear4)
                rc(gear3)
                c(gear2)

        elif gear2[2]==gear3[6]:
            if m[i][1]==1:
                if gear3[2]!=gear4[6]:
                    rc(gear4)
                c(gear3)  
            if m[i][1]==-1:
                if gear3[2]!=gear4[6]:
                    c(gear4)
                rc(gear3)
       
    if m[i][0]==4:
        if gear3[2]!=gear4[6]:
            if m[i][1]==1:
                c(gear4)
                if gear2[2]!=gear3[6]:
                    if gear1[2]!=gear2[6]:
                        rc(gear1)
                    c(gear2)
                rc(gear3)

            if m[i][1]==-1:
                rc(gear4)
                if gear2[2]!=gear3[6]:
                    if gear1[2]!=gear2[6]:
                        c(gear1)
                    rc(gear2)
                c(gear3)
        elif gear3[2]==gear4[6]:
            if m[i][1]==1:
                c(gear4)  
            if m[i][1]==-1:
                rc(gear4)       

if gear1[0]=='1':
    sum+=1
if gear2[0]=='1':
    sum+=2
if gear3[0]=='1':
    sum+=4
if gear4[0]=='1':
    sum+=8
print(sum)