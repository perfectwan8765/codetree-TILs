n, m = map(int, input().split())

arr = [
    [0]*m
    for _ in range(n)
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0
d = 0
arr[x][y] = 1
for i in range(2, n*m+1):
    ix = x + dx[d]
    iy = y + dy[d]

    if  ix < 0 or iy <0 or ix>=n or iy>= m or arr[ix][iy] != 0 :
        d = (d+1)%4
    x += dx[d]
    y += dy[d]

    arr[x][y] = i

for i in range(n):
    print(*arr[i])