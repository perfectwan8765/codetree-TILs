n = int(input())
arr = list(map(int, input().split()))

mm = 0
for i in range(n-1):
    s = arr[i]
    m = 0
    for j in range(i+1, n):
        d = arr[j] - s
        m = max(m, d)
    mm = max(mm, m)
print(mm)