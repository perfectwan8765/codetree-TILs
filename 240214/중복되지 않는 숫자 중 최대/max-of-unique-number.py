n = int(input())
arr = list(map(int, input().split()))

m = arr[0]
cnt = 1

for a in arr[1:]:
    if a > m :
        m = a
        cnt = 1
    elif a == m :
        cnt += 1

if cnt == 1:
    print(m)
else:
    print(-1)