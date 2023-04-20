# Wap to demonstrate multi_inheritance

class mobile():
    def __init__(self,company,color,price):
        self.company = company
        self.color = color
        self.price = price
    def Print_details(self):
        return f'{self.company} {self.color} {self.price}'
class smart_phone(mobile):
    def __init__(self,company,color,price,year):
        mobile.__init__(self,company,color,price)
        self.year = year

p1 = mobile("Apple","white","50000")
p2 = smart_phone("Blueberry","Black","45000","2017")

print(p1.Print_details())
print(p2.Print_details())