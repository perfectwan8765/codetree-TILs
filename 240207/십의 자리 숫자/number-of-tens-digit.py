l = list(map(int, input().split()))
result = [0]*10

for n in l :
    if n == 0:
        break
    x = n//10
    result[x] += 1

for i in range(1, 10):
    print(f"{i} - {result[i]}")