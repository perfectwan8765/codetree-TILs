n, m = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

x, y = 0, 0
end = n*m
result = [
    [0]*m
    for _ in range(n)
]
dirs = 0
result[x][y] = 1
for i in range(2, end+1):
    ix = x + dx[dirs]
    iy = y + dy[dirs]
    
    if ix < 0 or iy < 0 or ix >= n or iy >= m or result[ix][iy] != 0 :
        dirs = (dirs+1)%4
        ix = x + dx[dirs]
        iy = y + dy[dirs]
    x = ix
    y = iy
    result[x][y] = i

for i in range(n) :
    print(*result[i])