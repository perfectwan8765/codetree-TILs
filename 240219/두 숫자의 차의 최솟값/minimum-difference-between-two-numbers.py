n = int(input())
arr = list(map(int, input().split()))

x = arr[1] - arr[0]

for i in range(2, n):
    x = min(x, arr[i] - arr[i-1])

print(x)