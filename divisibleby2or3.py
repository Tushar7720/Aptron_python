#wap to print numbers that arent divisible by 2 and 3 in range

n = int(input("Enter the range : "))

i =0

while i <= n:
    if i % 2 != 0:
        if i % 3 != 0:
            print(i,"is not divible by 2 or 3")
    i += 1