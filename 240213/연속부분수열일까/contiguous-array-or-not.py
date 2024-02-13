n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i, n in enumerate(a) :
    if i > n1-n2 :
        print('No')
        break
    if n == b[0] :
        print(n)
        chk = 0
        for j, x in enumerate(b) :
            if x != a[i+j]:
                chk = 1
                break
        if chk == 0 :
            print('Yes')
            break