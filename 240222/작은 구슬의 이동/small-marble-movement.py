n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
mapper = {
    'U':0,
    'R':1,
    'L':2,
    'D':3
}
di = mapper[d]
for _ in range(t):
    x = c + dx[di]
    y = r + dy[di]

    if x < 1 or y < 1 or x >=n+1 or y >=n+1 :
        di = 3-di
        x = c
        y = r
    else:
        c = x
        r = y
print(r, c)