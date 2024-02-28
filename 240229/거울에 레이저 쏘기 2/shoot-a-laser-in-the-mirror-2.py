n = int(input())

arr = [
    input()
    for _ in range(n)
]

start = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

if start <= n :
    i = 0
    x = 0
    y = start-1
elif start <= n*2 :
    i = 1
    x = start-n-1
    y = n-1
elif start <= n*3 :
    i = 2
    x = n-1
    y = n - (num - 2*n)
else :
    i = 3
    x = n - (num - 3*n)
    y = 0

result = 0
while(True):
    if x < 0 or y < 0 or x >= n or y >= n :
        break
    
    mirror = arr[x][y]
    if mirror == '/':
        i = i ^ 1
    else :
        i = 3 - i

    x += dx[i]
    y += dy[i]

    result += 1
    
print(result)