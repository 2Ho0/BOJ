import sys
n = int(input())
num = []
stack = []
result = []
pm = []

j=1
for i in range(n):
    num.append(int(sys.stdin.readline()))

# for i in range(n-2):
#     if n<=2:
#         break

#     if (num[i]-num[i+1]>=2) and (num[i]>num[i+2]):
#         print('NO')
#         exit(0)
#     if n==3:
#         break

# for i in range(n-2):
#     for j in range(n):
#         num[i]-

while (j <= num[0]):
        stack.append(j)
        pm.append("+")
        j+=1

if n==1:
    pm.append("-")
    for i in range(len(pm)):
        print(pm[i])
    exit(0)
for i in range(n-1):
    if i==0:
        count=num[0]
    elif i>num.index(max(num)):
        count = num[i]
    else:
        count = max(result)
    
    if num[i]<num[i+1]:
        if i==0:
            a=stack.pop()
            result.append(a)
            pm.append("-")
        for _ in range(num[i+1]-count):
            stack.append(count+1)
            pm.append("+")
            count+=1

        a=stack.pop()
        result.append(a)
        pm.append("-")
    elif num[i]>num[i+1]:
        if i==0:
            a=stack.pop()
            result.append(a)
            pm.append("-")
        for _ in range(count-num[i+1]):
            if not stack:
                for i in range(len(pm)):
                    print(pm[i])
                exit(0)
            a=stack.pop()
            result.append(a)
            pm.append("-")

if num != result:
     print("NO")
     exit(0)
else:
    for i in range(len(pm)):
        print(pm[i])
            
    # if num[i]<num[i+1]:
    #     if i==0:
    #         a=stack.pop()
    #         result.append(a)
    #         print("-")
    #     while (count < num[i+1]):
    #         stack.append(count+1)
    #         print("+")
    #         count+=1

    #     a=stack.pop()
    #     result.append(a)
    #     print("-")
    # elif num[i]>num[i+1]:
    #     while (count >= num[i+1]):
    #         if not stack:
    #             exit(0)
    #         a=stack.pop()
    #         result.append(a)
    #         print("-")
    #         count-=1
  
        
        
    
    

