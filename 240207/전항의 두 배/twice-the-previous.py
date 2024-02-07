l = list(map(int, input().split()))

for i in range(2, 10):
    x1 = l[i-2]
    x2 = l[i-1]
    y = x2 + (x1*2)
    l.append(y)

print(*l)