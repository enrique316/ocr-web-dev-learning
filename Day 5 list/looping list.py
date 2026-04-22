"""
1. What is Looping a List?
👉 Looping means going through each item in a list one by one
👉 Used when you want to process every element
"""
a = [1,2,3,4]
for i in a:
    print(i) 

# another example #

c = ["name", "age", "Country"]
for d in c:
    print(c)


# another example # 
x = [2,3,4]
for y in x:
    print(y*3)
# another example #

details = ["name", "address", "phone no"]
for z in details:
    print(len(z))

# another example # 
invoice_data = ["name", "address", 7000, True]
for finale_data in invoice_data:
    if finale_data == 7000:
        print(finale_data)

# OCR examples # 

extracted_data = ["Name:ABD Associates","Address: India", "Amount:$50000", "Data:17-11-2027", "Data Complete: True" ]
for n in extracted_data:
    print(n)
for x in extracted_data:
    if x == "Amount:$50000":
        print(x)
