"""
1. What is immutability?
👉 Immutability means:
👉 “Once a tuple is created, it cannot be changed”
"""
"""
x = (1,2,3,4)
x[0]= 7
print(x) # this will through error . Tuple is inmutable. in order to change the any index postion value you need to 
convert tuple into list
 """ 
x = (1,2,3,4)
y = (list(x))
y[0] = 7
print(type(y))
print(y)


# try with append an index position value #  
"""
invoice_data = ("name","address")
invoice_data.append("phone no")
print(invoice_data) """ # doesnt work with tuple # 

