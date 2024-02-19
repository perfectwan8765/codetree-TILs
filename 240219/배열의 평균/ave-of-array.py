arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))
s = 0
for i in range(2):
    s += sum(arr[i])
    print(f"{sum(arr[i])/4:.1f}", end=" ")
print()
for i in range(4):
    print(f"{(arr[0][i] + arr[1][i])/2:.1f}", end=" ")
print()
print(f"{s/8:.1f}")