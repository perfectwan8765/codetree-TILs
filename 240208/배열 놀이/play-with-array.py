n, qn = map(int, input().split())
l = list(map(int, input().split()))

for x in range(0, qn):
    ql = list(map(int, input().split()))
    q = ql[0]
    a = ql[1]

    if q == 1 :
        print(l[a-1])
    elif q == 2:
        if a in l :
            print(l.index(a)+1)
        else :
            print(0)
    else :
        b = ql[2]
        print(*l[a-1:b:])