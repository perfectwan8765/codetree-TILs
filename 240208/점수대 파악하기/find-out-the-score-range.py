l = list(map(int, input().split()))

result = [0]*11

for n in l :
    if n == 0 :
        break
    result[n//10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {result[i]}")