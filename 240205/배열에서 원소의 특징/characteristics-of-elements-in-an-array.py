l = list(map(int, input().split()))

for i, n in enumerate(l) :
    if n%3 == 0 :
        print(l[i-1])
        break