def prime_WR(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1   

n = int(input("Enter a number to check prime or not (without recursion): "))

if prime_WR(n) == 1:
    print("It is prime")
else:
    print("Not prime")
