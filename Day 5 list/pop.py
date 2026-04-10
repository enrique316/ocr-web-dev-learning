# .pop() in python # 
list_1 = [1,2,3,4]
list_1.pop(0)
print(list_1)

# what if no index value is provided # 

x = [1,2,3,4]
x.pop()
print(x)

"""pop() Returns Value (Important) """

a = [20,30,40]
b = a.pop()
print(b)

# lets try with OCR example # 
invoice_data = ["name", "address", 1000 ]
remove_data = invoice_data.pop()
print("amount:", remove_data)
print(invoice_data)

# lets try another method # 
bill_of_lading = ["Glax  Shipping", "North Ireland", "12-jan-2026"]
filter_data = bill_of_lading.pop()
print("date:", filter_data)

# task #
a = [100, 200, 300, 400]
a.pop(0)
a.pop()
print(a)