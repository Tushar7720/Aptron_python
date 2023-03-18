# wap to calculate grade

'''
so the scheme would be :
if a student gets 0 - 20 % marks thats f grade
20- 50 % d grade
50 - 70 % c grade
70 - 90% b grade
90 - 100 % a grade
'''

n = int(input("Enter your marks :"))


if n>=0 and n<=20:
    print(" i am sorry you have failed ( F Grade")

elif n > 20 and n<=50:
    print(" Congrats you have passed but with D grade")

elif n >50 and n<= 70:
    print(" congrats you have passed with c grade ")

elif n >70 and n<=90:
    print(" Congrats you passed with a b grade ")

else:
    print("Congratulations You scored an A Grade")