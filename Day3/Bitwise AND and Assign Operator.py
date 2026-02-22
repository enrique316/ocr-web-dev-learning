# Bitwise AND and Assign Operator in python #

x = 2
x &= 3
print(x)

#another example 3

a = 4
a &= 1
print(a) 

#two digit example #

y = 10
y &= 7
print(y)   

#boolean scenario# 
a = False
b = True 
a &= b 
print(a)

z = True
y = False
z &= y 
print(z)

#with sets {} example #

h = {1,2,3}
c = {2,5,6} 
h &=c 
print(h) 

#string examples# 
list1_names = {"deeti", "gauri", "Jaggu"}
list2_names = {"deeti", "gauri"}

list1_names &= list2_names
print(list1_names) 

#ocr examples #

extracted_values = {"name","address", "mobileno",}
real_document = {"name", "address", "email"}
extracted_values &= real_document
print(extracted_values)

