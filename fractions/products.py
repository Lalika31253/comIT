# Operator Overloading
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

class Product:
  """_summ"""
    # constractor
  def __init__(self, name, price):
    self.name = name
    self.price = price

#Operator(s) overloading
  def __add__(self, other): # +
    # return self.price + other.price jusst for two items, not for iterable
    if isinstance(other, Product):
      return Product(f"{self.name}+{other.name}", self.price + other.price)
    return Product("Total", self.price + other)

# start = 0 to fix the error
# for item in cart:
#   start += item
def __radd__(self, other):  
  if other == 0:
    return self
  return self.__add__()

# for print(apple + orange*6 + chips)
def _mul__(self, number):
  return Product(f"{number} {self.name}s", self.price * number)

# CLI represention  
  def __str__(self):
    """user friendly"""
    return f"{self.name}: ${self.price}"
  
  def __repr__(self):
    """developer friendly (developer focus representation)"""
    return self.__str__() # transform object to the string representation from [<__main.Product]

  
apple = Product("Apple, 2.55")
orange = Product("Orange", 1.88)
chips = Product("Lays", 4.99)
  
print(apple, orange)
print(apple + orange*6 + chips)

cart = []
cart.append(apple)
cart.append(orange)
cart.append(chips)

print(cart)
print("Total in cart:", sum(cart))

# start = 0
# for item in cart:
#   start += item

# for prod in cart:
#   print(prod)