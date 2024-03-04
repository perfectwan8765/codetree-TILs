n = int(input())

x, y = n//2, n//2

arr = [
    [0]*n
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


arr[x][y] = 1
d = 0
chk = 2
dup = 1
flag = 1
for i in range(2, n**2+1):
    x += dx[d]
    y += dy[d]
    arr[x][y] = i
    flag += 1

    if i == chk :
        d = (d+1)%4
        chk += dup
        if flag == 2 :
            flag = 0 
            dup += 1

for i in range(n):
    print(*arr[i])