n = int(input())
result = 0
num = []

def is_beautiful():
    i = 0
    while i < n:

        if i+num[i]-1 >= n:
            return False

        for j in range(i, i+num[i]):
            if num[i] != num[j]:
                return False
        
        i += num[i]
    return True

def make(cnt):
    global result
    if cnt == n :
        if is_beautiful():
            result += 1
        return
    
    for i in range(1, 5):
        num.append(i)
        make(cnt+1)
        num.pop()

make(0)
print(result)