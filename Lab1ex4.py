n = int(input("Enter a number? "))

if n <= 0:
    print("is not a perfect number")
else:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i  
    if sum == n:
        print("is a perfect number")
    else:
        print("is not a perfect number")