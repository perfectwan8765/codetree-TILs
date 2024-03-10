n = int(input())

def fact_sum(n):
    if n == 1:
        return 1
    return fact_sum(n-1) + n
print(fact_sum(n))