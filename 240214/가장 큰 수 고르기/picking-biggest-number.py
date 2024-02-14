arr = list(map(int, input().split()))

chk = 0
for n in arr:
    chk = max(n, chk)
print(chk)