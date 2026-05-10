"""
1. What is get() method?

👉 get() is a dictionary method used to safely access values.
d.get('name')
"""
a = {
    'invoice_id': 45602, 
    'date': "12Jan1970"
}
print(a.get('invoice_id'))
#now with missing key # 
print(a.get('Amount'))
