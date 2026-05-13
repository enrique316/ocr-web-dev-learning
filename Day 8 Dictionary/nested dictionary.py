"""
👉 Nested dictionary means:

“A dictionary inside another dictionary”

👉 Instead of storing only simple values:

'name': 'John'

we can store:

'name': {
    ...
}
2. Why nested dictionaries are important

👉 Real-world data is often hierarchical.

Examples:

invoices
APIs
JSON
OCR data
user profiles
banking systems

👉 One dictionary contains another dictionary.

3. Basic syntax
d = {
    'key1': {
        'inner_key': value
    }
}
"""

name = {
   
   'mine': {
        
        'A':"hi",
        'B': "bye"
    }
}

print(name)

# another example # 
extract_data = {
    'finale_Data':{
        'InvoiceID': "560FHG",
        'amount': 3450
    }
}
print(extract_data)

#  multiple nested dictionary # 

data = {
    "classA1":
    {
        'name': "parteek",
        'Roll_no': 12
    },


'ClassB1':
{
    'name1': "Jyoti",
    'Roll_no1': 16
}

}

print(data)

# OCR example#

school = {

    'class': "A1",
    'subjects':{
        'English': "yes",
        'Maths': "Yes",
        'Science': "no"
    },

'total_subjects': 3
}


print(school)
