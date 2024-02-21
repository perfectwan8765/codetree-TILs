n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
for i in range(n):
    for j in range(n):
        chk = 0
        for k in range(4):
            x = dx[k]+i
            y = dy[k]+j

            if x < 0 or y < 0 or x >= n or y >= n :
                continue
            
            if arr[x][y] == 1:
                chk += 1
        if chk >= 3:
            result += 1
print(result)