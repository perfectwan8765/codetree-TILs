n, k = map(int, input().split())
arr = []

def main(i) :
    if i == n :
        print(*arr)
        return
    
    for j in range(1, k+1):
        arr.append(j)
        main(i+1)
        arr.pop()
main(0)