n = 3

arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))
input()
arr2 = []
for i in range(n):
    arr2 = list(map(int, input().split()))
    for j in range(n):
        print(arr1[i][j]*arr2[j], end=" ")
    print()