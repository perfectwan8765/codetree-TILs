result = 0
for i in range(4):
    arr = list(map(int, input().split()))
    result += sum(arr[:i+1:])
print(result)