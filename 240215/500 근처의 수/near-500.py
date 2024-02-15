arr = list(map(int, input().split()))

ma = 0
mi = 1000

for n in arr:
    if n < 500:
        ma = max(ma, n)
    elif n > 500:
        mi = min(mi, n)
print(ma, mi)