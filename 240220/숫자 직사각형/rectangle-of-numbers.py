n, m = map(int, input().split())
x = 1
for _ in range(n):
    for _ in range(m):
        print(x, end=" ")
        x += 1
    print()