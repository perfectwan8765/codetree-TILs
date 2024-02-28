n = int(input())

arr = [
    input()
    for _ in range(n)
]

start = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
i = 0
chk = 0
for _ in range(start-1):
    x += dx[i]
    y += dy[i]

    chk += 1
    if chk == n :
        i += 1
i = (i+1)%4
result = 0

while(True):
    result += 1
    mirror = arr[x][y]
    if mirror == '/':
        if i == 0 :
            i = 3
        if i == 2 :
            i = 1
        if i == 3 :
            i = 0
        if i == 1 :
            i = 2
    else :
        if i == 1 :
            i = 0
        if i == 0 :
            i = 1
        if i == 2 :
            i = 3
        if i == 3 :
            i = 2

    x += dx[i]
    y += dy[i]

    if x < 0 or y < 0 or x >= n or y >= n :
        break
print(result)