n = (int(input("Enter a number:")))
if n < 2:
    print("Not a prime number")
elif n==2:
    print("Is a prime number")
else:
    for i in range(2,n):
        if n% i==0:
            print("Is a prime number")
        else:
            print("Is a prime number")
            break
