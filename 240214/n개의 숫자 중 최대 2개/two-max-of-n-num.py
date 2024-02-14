n = int(input())
arr = list(map(int, input().split()))

if arr[0] > arr[1]:
    max1 = arr[0]
    max2 = arr[1]
else: 
    max1 = arr[1]
    max2 = arr[0]

for a in arr[2:]:
    if a > max1 :
        max1, max2 = a, max1
    elif a > max2 :
        max2 = a
print(max1, max2)