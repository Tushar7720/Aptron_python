# Python Program to Read a Number n and Compute n+nn+nnn

import math

n = int(input("Enter value of n :"))

Result = n + pow(n,2) + pow(n,3)

print(" The result fot the computation of n + nn + nnn where valu of n is",n," = ", Result)