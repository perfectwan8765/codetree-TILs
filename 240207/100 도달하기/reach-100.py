n = int(input())
result = [1, n]

i = 2
while(True) :
    x1 = result[i-2]
    x2 = result[i-1]
    y = x1 + x2
    result.append(y)

    if y > 100 :
        break
    i += 1
print(*result)