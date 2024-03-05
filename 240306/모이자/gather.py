import sys
n = int(input())
man = list(map(int, input().split()))

max_num = sys.maxsize
for i in range(n):
    stage_num = 0
    for j in range(n):
        stage_num += (abs(i-j)*man[j])
    max_num = min(max_num, stage_num)
print(max_num)