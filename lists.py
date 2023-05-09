# Nested lists

a = [1,2,["raman",11,112,233],12,34,56]

# to get raman

print(a[2][0])
# list with slicing

print(a[2][0][2::]) # prints man from raman

# negative slicing
print(a[2][0][::-1])

print(a[2][0][4::-1])

# Id function

a =10
b = 10
c = 10
print(id(a))
print(id(b))
print(id(c))
print()
print()
v = [1,2,3]
print(id(v))
v[0]="ram"
print(id(v))
