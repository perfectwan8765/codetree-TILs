d_arr = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i = 0
x, y = 0, 0
for d in d_arr:
    if d == 'L':
        i -= 1
    elif d == 'R':
        i += 1
    elif d == 'F':
        x += dx[i]
        y += dy[i]
    
    if i == -1 :
        i == 3
    elif i == 4 :
        i == 0
print(x, y)