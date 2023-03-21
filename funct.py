# wap to demontsrate Functions
'''
Functions are of 2 types : user defined and predefined
user defined are further of three types :
1. empty
2. parametrized
3. default

WAP to print numbers in a range using for loops and functions
'''

def numprint(n): # parametrized
    for i in range(1,n+1):
        print(i)

num = int(input("Enter a number :"))
numprint(num)
print("_____________________________________")

def numprint2(n=10): # default
    for i in range(1,n+1):
        print(i)

numprint2()
print("_____________________________________")

def numprint3(): # empty
    for i in range(1,11):
        print(i)

numprint3()