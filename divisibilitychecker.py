# Python Program to Print All Numbers in a Range Divisible by a Given Number

n = int(input("Enter range : "))
Divisor= int(input("Enter the numbers whose divisibility you want to check"))
i = 1
while i<=n:
    if i % Divisor == 0:
        print(i,"is divisioble by ",Divisor)
    i +=1