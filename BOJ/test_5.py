import numpy as np
n = list(map(int, input().split()))
hand = input()
phone = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

l_place = 10
r_place = 12

for i in n:
    distance = [0,0]
    if i == 0:
        i=11

        d1 = np.where(phone==l_place)
        d2 = np.where(phone==r_place)
        distance[0]=abs(d1[0][0]-3)+abs(d1[1][0]-1)
        distance[1]=abs(d2[0][0]-3)+abs(d2[1][0]-1)
        if distance[0]<distance[1]:
            l_place=i
            print("L", end='')
        if distance[0]>distance[1]:
            r_place=i
            print("R", end='')
        if distance[0]==distance[1]:
            if hand == 'left':
                l_place=i
                print("L", end='')
            if hand == 'right':
                r_place=i
                print("R", end='')
        continue
    if i==1:
        l_place=i
        print("L", end='')

        continue
    if i==4:
        l_place=i
        print("L", end='')

        continue
    if i==7:
        l_place=i
        print("L", end='')

        continue
    if i==3:
        r_place=i
        print("R", end='')

        continue
    if i==6:
        r_place=i
        print("R", end='')

        continue
    if i==9:
        r_place=i
        print("R", end='')

        continue
    if i==2:
        d1 = np.where(phone==l_place)
        d2 = np.where(phone==r_place)
        distance[0]=abs(d1[0][0]-0)+abs(d1[1][0]-1)
        distance[1]=abs(d2[0][0]-0)+abs(d2[1][0]-1)
        if distance[0]<distance[1]:
            l_place=i
            print("L", end='')
        if distance[0]>distance[1]:
            r_place=i
            print("R", end='')
        if distance[0]==distance[1]:
            if hand == 'left':
                l_place=i
                print("L", end='')
            if hand == 'right':
                r_place=i
                print("R", end='')
        continue
    if i==5:
        d1 = np.where(phone==l_place)
        d2 = np.where(phone==r_place)
        distance[0]=abs(d1[0][0]-1)+abs(d1[1][0]-1)
        distance[1]=abs(d2[0][0]-1)+abs(d2[1][0]-1)
        if distance[0]<distance[1]:
            l_place=i
            print("L", end='')
        if distance[0]>distance[1]:
            r_place=i
            print("R", end='')
        if distance[0]==distance[1]:
            if hand == 'left':
                l_place=i
                print("L", end='')
            if hand == 'right':
                r_place=i
                print("R", end='')
        continue
    if i==8:
        d1 = np.where(phone==l_place)
        d2 = np.where(phone==r_place)
        distance[0]=abs(d1[0][0]-2)+abs(d1[1][0]-1)
        distance[1]=abs(d2[0][0]-2)+abs(d2[1][0]-1)
        if distance[0]<distance[1]:
            l_place=i
            print("L", end='')
        if distance[0]>distance[1]:
            r_place=i
            print("R", end='')
        if distance[0]==distance[1]:
            if hand == 'left':
                l_place=i
                print("L", end='')
            if hand == 'right':
                r_place=i
                print("R", end='')
        continue
    
    
    