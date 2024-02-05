n = int(input())
chk = 0
l = [n]
for i in range(2, 11):
    x = n*i
    l.append(x)
    if x % 5 == 0:
        chk += 1
        if chk == 2:
            break
print(*l)