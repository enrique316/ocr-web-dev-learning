"""whatever users types in the input it is always stored as string"""

username = input("enter your username: ")
print(type(username))

age =input("enter your age: ")
converted_value = int(age)
print(type(converted_value))


invoice_amount = input("enter amount :")
invoice_number = input("enter invoice no:")
converted_amount = int(invoice_amount)
converted_number = int(invoice_number)
print(converted_amount + converted_number)


