n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = ['E', 'S', 'W', 'N']

x, y = 0, 0
for _ in range(n):
    a, b = input().split()
    b = int(b)
    d = arr.index(a)
    x += dx[d]*b
    y += dy[d]*b
print(x, y)