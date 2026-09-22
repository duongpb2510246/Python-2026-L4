def factor(n):
    re = 1
    for i in range(1,n+1):
        re *= i
    return re
print(factor(5))
print(factor(0))