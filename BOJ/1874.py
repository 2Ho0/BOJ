n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ""
for i in range(n):
    temp = a[i]
    if temp >= num:
        while temp >= num:
            stack.append(num)
            answer += "+\n"
            num+=1
        stack.pop()
        answer += "-\n"
    else:
        s = stack.pop()
        if s > temp:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"
            
if result:
    print(answer)