l = list(map(int, input().split()))
t = l[2::3]

print(sum(l[1::2]), round(sum(t)/len(t), 1))