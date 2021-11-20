n = int(input())
len=len(str(n))
if n<11:#11보다 작으면 생성자가 없음
    if n%2==0:
        print(n//2)
        exit(0)
    print("0")
    exit(0)
for i in range(9*len):
    base = n-9*len+i
    if base<0:#base가 0이하가 되면 생성자가 있어도 생성자의 값이 올바르게 나오지 않기 때문에 0이상으로 바꿔줌
        base=abs(base)
    temp = base
    a = []
    for _ in range(len):
        a.append(temp%10)
        temp = temp//10
    if (base+sum(a)==n):
        print(base)
        exit(0)
print("0")