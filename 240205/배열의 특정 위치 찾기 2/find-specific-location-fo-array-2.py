l = list(map(int, input().split(" ")))

x = sum(l[::2])
y = sum(l[1::2])

print(max(x, y) - min(x, y))