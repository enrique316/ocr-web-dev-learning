# .insert in list # 
"""1. What is insert()?

insert() means:

👉 Adding an item at a specific position
👉 Not just at the end

It allows controlled placement """

name = [4,2,3]
name.insert(1,17)
print(name)

# example with string # 
class_details = ["First","third", "Second"]
class_details.insert (1,"Second")
print(class_details)

# Insert Beyond Range (Important) #
x = [1,2]
x.insert(10,3)
print(x)

# .insert vs .append # 
y = [1,2,3,4]
x.insert(0,0)
print(x)
#now .append # 
x.append(0)
print(x)

# OCR example # 
invoice_data = ["INV2345", 4500]
invoice_data.insert(1,"12Jan2027")
print(invoice_data)