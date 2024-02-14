n = int(input())
arr = list(map(int, input().split()))

end = n
result = []
while (True):
    m = 0
    for i in arr[:end:]:
        if i > m:
            m = i 
    end = arr.index(m)
    result.append(end+1)

    if end == 0:
        break
print(*result)