""" What is key argument in python"""
""" A Keyword Argument is an argument where you pass a value to a function by using the parameter's name.

Instead of relying on the order of values, you explicitly tell Python which parameter should receive each value."""
def info(name, age):
    print(name, age)
info(name="shubhankar", age=37)
#---#

def data(invoice, address, amount, tax):
    print(invoice, address, amount, tax)
data(invoice ="INV345", address="NYC", amount=70000, tax= 18)

#another example# 
def fun(price, tax, discount):
    return price + tax - discount
finale_price = fun(
    price= 70000,
    tax= 700,
    discount=5600 
)
print(finale_price)