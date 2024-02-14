n = int(input())
arr = list(map(int, input().split()))

m = 0
chk = [0]*1001

for a in arr :
    chk[a] += 1

if 1 not in chk :
    print(-1)

for i in range(1000, 0, -1):
    if chk[i] == 1:
        print(i)
        break