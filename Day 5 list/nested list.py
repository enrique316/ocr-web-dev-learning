# Nested list # 
"""
1. What is a nested list?
👉 A nested list means:
👉 “A list inside another list”
"""

a = [[1,2,], [3,4]]
print(a)

# accessing individual list from nested list #

x = [[1,2],[3,4],[4,5]]
print(x[0])
print(x[1])
print(x[2])

# accessing single values from nested list #

xy = [[1,2,3],[3,4,5]]
print(xy[0][0])
print(xy[1][0])

# loop inside nested list #
ab = [[1,2,3], [4,5,6]]
for cd in ab:
    print(cd)

# loop inside nested list #

name = [[5,6,7], [8,9,10]]
for destination in name:
    for role in destination:
        print(role)

# another simmilar example # 
invoice_data = [['invoice_id', 'address'], ['amount', 'date']]
for data in invoice_data:
    for finale_date in data:
        print(finale_date)

# OCR example # 


user_data = [['name','last name'], ['age', 'DOB']]
for details in user_data:
    for finale_data in details:
        print(finale_data)

# Accessing on single value from list 

