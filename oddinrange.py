# wap to print all odd numbers in range

n = int(input("Enter the Range :"))

i = 0

while i <= n:
    if i % 2 != 0:
        print(i,"is odd")
    i += 1