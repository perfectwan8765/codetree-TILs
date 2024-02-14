n = int(input())
arr = list(map(int, input().split()))

m = 0
chk = [0]*1001

for a in arr :
    chk[a] += 1

if 1 not in chk :
    print(-1)
else:
    print(chk.index(1)+1)