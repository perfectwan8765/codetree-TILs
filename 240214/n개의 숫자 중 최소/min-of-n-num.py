N = int(input())
arr = list(map(int, input().split()))

chk = arr[0]
cnt = 1
for n in arr[1:]:
    if n < chk :
        chk = n
        cnt = 1
    elif n == chk :
        cnt += 1

print(chk, cnt)