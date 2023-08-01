from classes.order  import Order

class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "name"):
            self._name - value
        else:
            raise Exception
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customer(self):
        pass

    def num_orders(self):
        pass

    def average_price(self):
        pass

    
# class Coffee:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         if hasattr(self, "name"):
#             raise Exception
#         elif isinstance(value, str):
#             self._name = value

#     def orders(self):
#         from classes.order import Order
#         return [order for order in Order.all if order.coffee == self]

    
#     def customers(self):
#         from classes.customer import Customer
#         return list(set([order.customer for order in self.orders()]))

    
#     def num_orders(self):
#         return len(self.orders())
    
#     def average_price(self):
#         total_price = [order.price for order in self.orders() if order.coffee == self]
#         num_orders = len(total_price)
#         average_price = sum(total_price) / num_orders
#         return average_price