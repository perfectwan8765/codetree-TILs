arr = input()
n = len(arr)
result = 0
for i in range(n) :
    if arr[i] == '(':
        for j in range(i+1, n):
            if arr[j] == ')':
                result += 1
print(result)