a, b = map(int, input().split())
l = [0]*(b+1)

while(True):
    l[a%b] += 1
    a = a//b
    if a < 2:
        break
result = 0
for i in range(0, len(l)) :
    result += (l[i]**2)
print(result)