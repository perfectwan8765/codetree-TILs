n = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir_map = {
    'N':0,
    'W':1,
    'S':2,
    'E':3
}
x, y = 0, 0
result = 0
for _ in range(n):
    d_key, i = input().split()
    i = int(i)
    d = dir_map[d_key]
    for j in range(i):
        result += 1
        x += dx[d]
        y += dy[d]
        if x == 0 and y == 0:
            print(result)
            exit()
print(-1)