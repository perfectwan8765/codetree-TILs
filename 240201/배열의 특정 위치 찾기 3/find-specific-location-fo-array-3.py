a = list(map(int, input().split()))
l = len(a)

for n in range(0, l):
    if a[n] == 0:
        print(sum(a[n-3:n:1]))
        break