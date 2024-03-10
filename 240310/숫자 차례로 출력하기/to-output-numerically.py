n = int(input())

def print_num(n):
    if n == 0 :
        return

    print_num(n-1)
    print(n, end=" ")

def print_num_reverse(a, b):
    if a == b+1 :
        return

    print_num_reverse(a+1, b)
    print(a, end=" ")

print_num(n)
print()
print_num_reverse(1, n)