# Wap to demonstrate class methods

global model
global price
global brand

class laptop():
    @classmethod
    def From_string(cls,s):
        brand,model,price= s.split(",")
        for item in (brand,model,price):
            print(item)

l1 = laptop()
l1.From_string("HP,HP2023,45000")

