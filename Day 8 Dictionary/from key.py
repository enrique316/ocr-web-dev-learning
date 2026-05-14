"""
What is fromkeys()?

👉 fromkeys() is a dictionary method used to:

“Create a dictionary using a list of keys with same default value”

👉 Instead of manually writing:

{
    'a': 0,
    'b': 0,
    'c': 0
}

we can generate it automatically.

2. Basic syntax
dict.fromkeys(keys, value)
3. Basic example
d = dict.fromkeys(['a', 'b', 'c'], 0)

print(d)
"""

a = dict.fromkeys('Shubhankar',1)
print(a)

# another example# 
 
b = dict.fromkeys('Biswas', 1)
print(b)

# OCR example # 

extracted_feilds = [ 'name', 'address', 'amount', 'date']
final_feilds = dict.fromkeys(extracted_feilds, '')
print(final_feilds)