dirs = input()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
i = 0
result = 0
isExists = False
for d in dirs: 
    result += 1
    if d == 'F':
        x += dx[i]
        y += dy[i]
    elif d == 'R':
        i = (i+1)%4
    elif d == 'L':
        i = (i-1+4)%4
        
    if x == 0 and y == 0 :
        print(result)
        isExists = True
        break
if not isExists :
    print(-1)