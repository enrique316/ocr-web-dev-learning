"""
👉 A dictionary is a data structure that stores data in:

key : value

pairs.

👉 Example:

name : John
age : 25
city : Delhi

Here:

Key	Value
name	John
age	25
city	Delhi
2. Why dictionaries are important

👉 Dictionaries are heavily used in:

APIs
OCR systems
JSON data
AI systems
Web applications
Invoice extraction
Form processing

👉 Because real-world data usually comes as:

field : value

Example:

Invoice Number : INV001
Total : 5000
Date : 10-05-2026
"""
a = {
    'name': "Diti", 
    'Age': 7 
}
print(type(a))

# another example # 

x = {
    'name': "Shubhankar",
    'name':"Dimpal"
}
print(x) 
# Dictionary are mutable # 
ab = {
    'he_said': "hi", 
    'i_said': "bye"
}
ab ['he_said'] = "hello"
print(ab)
# another example #
a = {
    'invoiceID':"GHS123"
}
a['invoiceID']= "HJS123"
print(a)

