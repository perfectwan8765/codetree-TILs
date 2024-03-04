n = int(input())

x, y = n//2, n//2

arr = [
    [0]*n
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_dir, move_num = 0, 1
cnt = 1

while True :
    
    for _ in range(move_num):
        arr[x][y] = cnt

        cnt += 1
        x += dx[move_dir]
        y += dy[move_dir]
        
    if x < 0 or y < 0 or x >= n or y >= n :
        break

    move_dir = (move_dir+1) % 4
    
    if move_dir == 0 or move_dir == 2 :
        move_num += 1

for i in range(n):
    print(*arr[i])