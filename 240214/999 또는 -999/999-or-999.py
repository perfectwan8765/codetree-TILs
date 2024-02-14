arr = list(map(int, input().split()))

ma = -999
mi = 999

for n in arr :
    if n == 999 or n == -999:
        break
    mi = min(n, mi)
    ma = max(n, ma)
print(ma, mi)