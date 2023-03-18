# wap to find all divisors of a number

n = int(input("Enter a number : "))

i = 1

while i <= n:
    if n % i == 0:
        print(i,"is a divisor of ",n)
    i += 1