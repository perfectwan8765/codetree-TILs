num = input()
result = 0
for i in range(len(num)):
    n = int(num[i])
    n = (n+1)%2
    new_num = f"{num[:i]}{n}{num[i+1:]}"
    result = max(result, int(new_num, 2))
print(result)