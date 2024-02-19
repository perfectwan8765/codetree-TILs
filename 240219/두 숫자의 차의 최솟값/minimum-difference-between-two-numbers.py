n = int(input())
arr = list(map(int, input().split()))

x = 100
for i in range(n):
    for j in range(i+1, n):
        d = abs(arr[i]-arr[j])
        x = min(x, d)

print(x)