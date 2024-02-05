l = list(map(int, input().split()))

for i in range(2, 10):
    l.append((l[i-1] + l[i-2])%10)
print(*l)