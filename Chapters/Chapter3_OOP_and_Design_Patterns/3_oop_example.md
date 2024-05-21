## Object Oriented Thinking

- A class is a blueprint of objects
- Objects have attributes(data member or property) and methods(behavior)
- The functions defined inside the class are called methods. 
- To initialize the object attributes, __init__ method is used. This method is called implicitly at the time of object creation. But to access other instance methods, object should that method explicitly using dot operator. eg. obj.get_discounted_price()
- All instance methods of a class take "self" as a first argument. The "self" is the object that is calling that method at the point of time. 
- Instead of "self", you can write anything, but writing "self" is a general trend. 
- You have to use dot operator "." to access the attributes or methods of the object.  eg. object.name or object.get_name()

```python


# class definition
class Product:
    # initializer method, its called when the object is created
    def __init__(self, name, price, discount, quantity, description=None):
        # attributes of the object self
        self.description = description
        self.name = name
        self.price = price
        self.discount = discount
        self.quantity = quantity

    def get_discounted_price(self):  # instance method
        discount_amount = self.discount * self.price / 100
        return self.price - discount_amount
    
    def sell_product(self, quantity_to_sell):    # instance method
        if self.quantity < quantity_to_sell:
            print("Insufficient quantity to sell")
        else:
            total_price = quantity_to_sell * self.get_discounted_price()
            print(quantity_to_sell, "item is sold for Rs. ", total_price)
            self.quantity = self.quantity - quantity_to_sell
            print(self.name, ":", self.quantity, "remaining now.")
    

# objects creation
product1 = Product("SD BOOK", 10000, 10, 15)
product2 = Product("Mobile Charger", 500, 0, 10, description="Excellent mobile charger")


# Calling objects attributes and methods
print(product2.quantity, "++++")
product2.sell_product(quantity_to_sell=3)
product2.sell_product(quantity_to_sell=2)
print(product2.quantity, "-----")

```