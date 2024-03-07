n = int(input())
cows = list(map(int, input().split()))

if n < 3 :
    print(0)
    exit()

result = 0
for i in range(n-2) :
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cows[i] <= cows[j] and cows[j] <= cows[k] :
                result += 1
print(result)