# object, instance, entity = object

class Product:
    # initializer method, its called when the object is created
    def __init__(self, name, price, discount, quantity, description=None):
        self.description = description
        self.name = name
        self.price = price
        self.discount = discount
        self.quantity = quantity

    def get_discounted_price(self):  # instance method that takes self as a first argument
        discount_amount = self.discount * self.price / 100
        return self.price - discount_amount
    
    def sell_product(self, quantity_to_sell):
        if self.quantity < quantity_to_sell:
            print("Insufficient quantity to sell")
        else:
            total_price = quantity_to_sell * self.get_discounted_price()
            print(quantity_to_sell, "item is sold for Rs. ", total_price)
            self.quantity = self.quantity - quantity_to_sell
            print(self.name, ":", self.quantity, "remaining now.")
    

product1 = Product("SD BOOK", 10000, 10, 15)
product2 = Product("Mobile Charger", 500, 0, 10, "Excellent mobile charger")

print(product2.quantity, "++++")
product2.sell_product(quantity_to_sell=3)
product2.sell_product(quantity_to_sell=2)
print(product2.quantity, "-----")

# https://github.com/ecedreamer/SoftwareDesign


product1.sell_product(quantity_to_sell=5)
