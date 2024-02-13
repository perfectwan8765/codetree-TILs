n = int(input())
arr = list(map(int, input().split()))

chk = 0 
for i, x in enumerate(arr) :
    if x == 2:
        chk += 1
    if chk == 3 :
        print(i+1)
        break