import sys
input = sys.stdin.readline

n, m = map(int, input().split())

wb = []
for i in range(4):
    wb.append(list("WBWBWBWB"))
    wb.append(list("BWBWBWBW"))

bw = []
for i in range(4):
    bw.append(list("BWBWBWBW"))
    bw.append(list("WBWBWBWB"))

a = []
countwb = 0
countbw = 0
answer = []
step1 = 0
step2 = 0

for i in range(n):
    a.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        for k in range(i,i+8):
            for l in range(j, j+8):
                if a[k][l] != wb[step1][step2]:
                    countwb += 1
                elif a[k][l] != bw[step1][step2]:
                    countbw += 1
                step2 += 1
            step1 += 1
            step2 = 0
        step1 = 0

        answer.append(countwb)
        answer.append(countbw)
        countwb = 0
        countbw = 0

print(min(answer))