# list length using len() # 
x = [1,2,3,4]
print(len(x))

# another example # 
list_a = [10,20,5, 7, 9]
print(len(list_a))

# counting length using different data types # 
ab = [20, "hi",3.5,True ]
print(len(ab))

# counting nested list (very important) # 
d = [[1,2], [4,5]]
print(len(d))

# other examples # 
a = [1,2,3,4]
if len(a)> 2:
 print("data valid")
else:
 print("data not valid")

# ocr examples # 

name = [["ram","shyam"], ['ramesh', 'suresh']]
print(len(name))

# another example # 
invoice_data = ["inv20", 34050, True]
if len(invoice_data) > 2:
 print("data valid")
else:
 print("data invalid") 