#Bitwise XOR Assignment Operator # 

a = 2
c = 4
a ^=c 
print(a)


#another example with complex scenario # 
a = 10
a ^= 3
a ^= 3 
print(a) 

#boolean with bitwise OXR #

x = True
y = False
x ^= y
print(x) 

#another examples with boolean #

x = True
y = True
x ^= y 
print(x) 

#with sets {} example 

extract_values = {1,2,3,4,5}
real_values = {1,2,3}
extract_values ^= real_values
print(extract_values)


# ocr examples #

caputured_features = { "tables", "rows", "columns", "lines"}
extracted_features = {"tables", "rows", "columns"}
caputured_features ^= extracted_features
print(caputured_features)