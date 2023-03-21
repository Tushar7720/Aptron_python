# wap to demonstrate for loops
# sum of all even numbers in a range

n = int(input("Enter the Range :"))
sum1 = 0
for i in range(1,n+1):
    if i % 2 ==0:
        sum1 = sum1 + i

print(sum1)