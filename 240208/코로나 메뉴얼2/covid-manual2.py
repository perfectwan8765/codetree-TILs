result = [0]*4
for _ in range(0, 3):
    patient = input().split()
    x = patient[0]
    c = int(patient[1])

    if x == 'Y':
        if c >= 37 :
            result[0] += 1
        else :
            result[2] += 1
    else:
        if c >= 37 :
            result[1] += 1
        else :
            result[3] += 1

if result[0] > 1 :
    e = "E"
else :
    e = ""
print(*result, e)