#wap Python Program to Find Sum of Digits of a Number

n = int(input(" Enter any number : "))
x =0
num = n
while n > 0:
    x = x + n % 10
    n = n//10


print("The sum of digits of ", num , "is", x)


