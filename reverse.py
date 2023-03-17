# to check if a number is a palindrome or not

n = int(input("Enter the numner you want to check"))
n_save = n
temp = 0
d =0

while n != 0:
    d = n % 10;
    temp = temp * 10 + d
    n = n // 10

print("The reversed number is : ", temp)

