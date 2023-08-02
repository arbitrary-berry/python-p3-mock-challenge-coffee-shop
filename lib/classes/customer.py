from classes.order import Order

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str and 1 <= len(value) <=15:
            self._name = value
        else:
            raise Exception("Name is invalid.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return [*set([order.coffee for order in self.orders()])]
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)



# from classes.order import Order

# class Customer:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         if type(value) == str and 1 <= len(value) <= 15:
#             self._name = value
#         else:
#             raise Exception

        
#     def orders(self):
#         from classes.order import Order
#         return [order for order in Order.all if order.coffee == self]
    
#     def coffees(self):
#         from classes.coffee import Coffee
#         return list(set([order.coffee for order in self.orders()]))

#     def create_order(self, coffee, price):
#         if type(price) == int:
#             new_order = Order(customer=self, coffee=coffee, price=price)
#             return new_order
#         else:
#             raise Exception