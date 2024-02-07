l = list(map(int, input().split()))
result = []

for n in l :
    if n == 0:
        break
    if n%2 == 0 :
        result.append(n//2)
    else:
        result.append(n+3)
print(*result)