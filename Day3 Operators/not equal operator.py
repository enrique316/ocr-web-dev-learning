# != comparison operator # 
"""not equal becomes true
and equal becomes false"""
a = 4
b =3
print ( a !=b)

#another example #

x = 10
y = 10
print( x !=y)

#example with strings# 

a = "cat"
b = "dog"

print(a !=b)


#example with list# 
y = [1,2,3]
x = [1,2]
print(y !=x)

# compare boolean with numbers #
a = "true" 
b = 1 
print(a !=b) 

user_logged_in = False
if user_logged_in != True:
    print("user not logged in")

#ocr examples #

invoice_values = 4500
extracted_value = 3500
if invoice_values != extracted_value:  
 print(" data mismatched ! check the file" )


