# wap to demonstrate lists

fruits = ['Apples', 'kiwi','orange']
print(fruits)

#adding elements
'''
Append : adds at the last of the list
Insert : adds at any given position 

'''
fruits.append('mango')
print(fruits)

fruits.insert(2,'watermelon')
print(fruits)

'''
Deleting elements:

pop : Delets from last and saves in buffer 
remove : removes from a specific place 

'''

fruits.remove('Apples')
print(fruits)

'''
extend command : Extends one list into another 
'''

l1 = [ 1,2,3,4]
l2 = [3,5,6,7,8]

l2.extend(l1)

print(l2)

# user input list

n = int(input("enter range"))
l3 = []
for i in range(n):
    num = int(input("Enter you number:"))
    l3.append(num)

print(l3)
