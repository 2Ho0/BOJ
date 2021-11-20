n,m = map(int, input().split())
tetromino = []
result = []
sum = 0
for i in range(n):
    tetromino.append(list(map(int, input().split())))

#1
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+1][j+2]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+2][j+1]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+2][j]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i+1][j]+tetromino[i+2][j]+tetromino[i+2][j+1]
        result.append(sum)
for i in range(n-3):
    for j in range(m):
        sum=tetromino[i][j]+tetromino[i+1][j]+tetromino[i+2][j]+tetromino[i+3][j]
        result.append(sum)

#2
for i in range(n-1):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i+1][j]+tetromino[i+1][j+1]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i+2][j+1]+tetromino[i+1][j+1]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i+1][j+2]+tetromino[i+1][j+1]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j+1]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+1][j+2]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j+1]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+2][j]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j+1]+tetromino[i][j+2]+tetromino[i+1][j]+tetromino[i+1][j+1]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j+1]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+2][j+1]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i+1][j]+tetromino[i+2][j]
        result.append(sum)
for i in range(n-2):
    for j in range(m-1):
        sum=tetromino[i][j+1]+tetromino[i+1][j+1]+tetromino[i+2][j]+tetromino[i+2][j+1]
        result.append(sum)

#3
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i][j+2]+tetromino[i+1][j]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i][j+2]+tetromino[i+1][j+1]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i][j+2]+tetromino[i+1][j+2]
        result.append(sum)
for i in range(n-1):
    for j in range(m-2):
        sum=tetromino[i][j+2]+tetromino[i+1][j]+tetromino[i+1][j+1]+tetromino[i+1][j+2]
        result.append(sum)

#4
for i in range(n):
    for j in range(m-3):
        sum=tetromino[i][j]+tetromino[i][j+1]+tetromino[i][j+2]+tetromino[i][j+3]
        result.append(sum)
print(max(result))