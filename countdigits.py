#wap Python Program to count number of Digits of a Number

n = int(input(" Enter any number : "))
x =0
num = n
count = 0
while n > 0:
    x = x + n % 10
    n = n//10
    count += 1


print("The number of digits of ", num , "is", count)