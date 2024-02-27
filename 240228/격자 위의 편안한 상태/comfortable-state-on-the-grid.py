n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

arr = [
    [0]*n
    for _ in range(n)
]

for _ in range(m):
    r,c = map(int, input().split())
    x,y = r-1, c-1
    arr[x][y] = 1
    chk = 0
    for i in range(4):
        ix = x + dx[i]
        iy = y + dy[i]

        if ix < 0 or iy < 0 or ix >=n or iy >=n :
            continue
        
        if arr[ix][iy] == 1 :
            chk += 1
    
    if chk == 3 :
        print(1)
    else :
        print(0)