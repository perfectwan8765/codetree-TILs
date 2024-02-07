l = list(map(int, input().split()))
result = [0]*7

for n in l :
    result[n] += 1

for i in range(1, 7):
    print(f'{i} - {result[i]}')