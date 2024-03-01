n, m = map(int, input().split())

arr = [
    [0]*m
    for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 0
c = 64
arr[x][y] = 'A'

for i in range(2, n*m+1):
    ch = c + (i+26)%26
    ix = x + dx[d]
    iy = y + dy[d]

    if ix < 0 or iy < 0 or ix >= n or iy >= m or arr[ix][iy] != 0 :
        d = (d+1)%4
    
    x += dx[d]
    y += dy[d]   

    arr[x][y] = chr(ch)

for i in range(n):
    print(*arr[i])