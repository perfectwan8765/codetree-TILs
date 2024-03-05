n, t = map(int, input().split())
dirs = input()

x, y = n//2, n//2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = arr[x][y]
move_dir = 0
for i in range(t):
    d = dirs[i]
    if d == 'R':
        move_dir = (move_dir+1)%4
    elif d == 'L':
        move_dir = (move_dir-1+4)%4
    elif d == 'F':
        ix = x + dx[move_dir]
        iy = y + dy[move_dir]

        if ix < 0 or iy < 0 or ix >= n or iy >= n :
            continue
        x = ix
        y = iy
        result += arr[x][y]
print(result)