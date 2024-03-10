n, k = map(int, input().split())
arr = []

def main(i) :
    if i == k :
        print(*arr)
        return
    
    for j in range(1, n+1):
        arr.append(j)
        main(i+1)
        arr.pop()
main(0)