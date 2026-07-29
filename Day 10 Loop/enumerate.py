# What is enumerate #
"""
names = [ "diti", "gauri", "Dhunni"]
for index, fruit in enumerate(names):
    print(index,":", fruit)
#example #
extracted_data = [
    "Invoice No",
    "Date",
    "time",
    "City",
]
for index, extracted_data in enumerate(extracted_data):
    print(index,"-", extracted_data) """ 

""" 
captured_data =[ 
    "Name",
    "amount",
    "-", 

]
for n, captured_data in enumerate(captured_data):
    print(n, ":", captured_data)

# OCR example # 
amount = [
    500,
    600, 
]

for x, amount in enumerate(amount):
    print(x, amount) """ 

student_list = [
    "ram",
    "shyam",
    "Sita", 
    "git"
]
for a, student_list in enumerate(student_list, start=1):
    print(a, ":", student_list)
