# wap to demonstrate OOPS

class laptop:
    brand = input("Please enter brand name: ")
    model = input("Please enter model name: ")
    price = int(input("Please enter price: "))
    def __init__(self):
        self.brand = laptop.brand
        self.model = laptop.model
        self.price = laptop.price

    def Calc_discounted():
        discount = float(input("Enter the discount percentage: "))
        off_price = (discount/100)*laptop.price
        print("Your price after discount is : ",laptop.price - off_price)

li = laptop
li.Calc_discounted()

