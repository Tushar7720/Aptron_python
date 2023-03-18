# wap to find smallest divisor of a number

n = int(input("Enter a number : "))

i = 2

while i <= n:
    if n % i == 0:
        print(i,"is the smallest divisor of ",n)
        break
    i += 1