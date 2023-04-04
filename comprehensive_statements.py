'''
Comprehensive statements
These statements only work on 1. lists 2. dictionaries
They read the code from bottom to top
They are used to shorten the code

'''
# Regular Code

num = [1,2,3,4,5,6]
square=[]
for i in num:
    if i % 2 ==0:
        square.append(i*i)
    else:
        square.append("Odd number")
print(square)

# comprehensive code for the regular code

square2= [i*i if i%2==0 else "Odd number" for i in num]
print(square2)