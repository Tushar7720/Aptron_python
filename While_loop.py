#Wap to demonstrate while loops
# find even numbers uptill a given number and print their sum

i = 1
n = int(input("Enter Number"))
sum1 = 0

while i<=n:
    if(i % 2 == 0):
        print(" Even number : ", i)
        sum1 += i
    i += 1
print("The Sum of these even numbers is :", sum1)


