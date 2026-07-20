# Break statement #
""" for number in range(7):
    if number == 3:
        break
    print(number) """ 

# example #
for data in range(2,10):
    if data == 6:
        break
    print(data)

# OCR examples #
"""captured_fields = [
    "name",
    "address",
    "phone no", 
    "ERROR"
    "Country"
    "amount"
]
for y in captured_fields:
    if y == "ERROR":
        break
    print(y) """

# Another example# 
extracted_data = [
    "name",
    "address",
    "phone no", 
    "ERROR",
    "Country",
    "amount",
]

for x in extracted_data:
    if x == "ERROR":
        break
    print("check data",x)

# Another example#
password = ["ladygaga434343"]
for y in password:
    if y == "adygaga434343":
        break
    print("valid", y)

# example# 
numbers = [1,2,3,4,5]
for n in numbers:
    if n == 4:
        print(n)

