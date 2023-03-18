# wap a Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

n = int(input("Enter any range :"))

i = 1
while i<=n:
    if i%7 == 0 and i%5 ==0:
        print(i, "Divisible by both")

    i += 1

