# Functions as variables In python #
def greeting():
    print("hi")
x =greeting
x()

def name():
    print("shubhankar")
a=name
a()

# another example #

def invoice():
    print("INVOICE-20-10-23")
def amount():
    print(70000)
a=invoice
b=amount
a()
b()