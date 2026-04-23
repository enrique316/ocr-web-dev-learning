# Single item tuple # 
# lets try and example # 
t = ("name")
print(type(t)) # the out put is string as it wasnt properly converted # 

x = "game"
y = tuple(x)
print(type(y)) # This one run correctly # 

# or you can use more accurate method # 
a = ("name",)
print(type(a))


# ocr example #
invoice_data = ("amount",)
print(invoice_data)