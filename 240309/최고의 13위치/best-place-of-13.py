n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n):
    for j in range(n-2):
        num = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        result = max(result, num)
print(result)