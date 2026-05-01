name = "shubhankar"
last_name = 'Biswas'
address = "Rewari"
Mobile_No = "9999999"
full_address = name + last_name + address + Mobile_No 
concatenation = name + " " + last_name + " " + address + " " + Mobile_No
print(full_address)
print(len(full_address))
print(concatenation)

#--------# 

my_name = "Dhu\nrand\thar"
last_name = "dhuranhar\rpart2"
print(my_name)
print(last_name)
#-----# 
x = "name", "address", "phone no"
print(x[2])


invoice_data = "name", "address", "phone"
if invoice_data[0] == "name":
    print("data valid")
else:
    print("data not valid")
    print(type(invoice_data))

# another example # 

extracted_data = "Invoice1764 address phone no "
if extracted_data[12:18] == "address":
    print("Data valid")
else:
    print("data not detected")

# reverse string # 

cd = "name ois diti"
print(cd[::-4])