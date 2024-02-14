N = int(input())
arr = list(map(int, input().split()))

chk = arr[0]
for n in arr[1:]:
    chk = min(n, chk)

result = 0
for n in arr :
    if n == chk:
        result += 1

print(chk, result)