n, m = map(int, input().split())

arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

for i in range(n):
    arr2 = list(map(int, input().split()))
    for j in range(m):
        x = 1
        if arr1[i][j] == arr2[j] :
            x = 0
        print(x, end=" ")
    print()