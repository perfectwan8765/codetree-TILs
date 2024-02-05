l = list(map(int, input().split()))

x = sum(l[::2])
y = sum(l[1::2])

mx = max(x, y)
mn = min(x, y)
print(mx - mn)