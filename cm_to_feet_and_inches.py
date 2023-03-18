# wap to convert cm to feet and inches

n = int(input("Enter value in centimeters :"))

inches = n / 2.54

remainder_inches = inches % 12
feets = inches// 12

print(n,"cms =",feets,"feets and",remainder_inches,"inches. ")