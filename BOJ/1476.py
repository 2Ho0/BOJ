a,b,c = map(int, input().split())
e = []
s = []
m = []
for i in range(532):
    E=15*i+a
    S=28*i+b
    M=19*i+c

    e.append(E)
    s.append(S)
    m.append(M)
    if E in s:
        for j in range(len(m)):
            if E == m[j] and m[j] in s:
                print(m[j])
                exit(0)
    




