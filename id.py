invoice_number = 10
print(id(invoice_number)) 


#two variables with same value
invoice_number1 = 100
invoice_number2 = 100
print(id(invoice_number1))
print(id(invoice_number2))

#list with ID 
invoice_list = [1,2,3]
invoice_list2 = [1,2,3]
print(id(invoice_list))
print(id(invoice_list2))

#assigning one variable to another
list1 = [1,2,3]
list2 = list1
print(id(list1))
print(id(list2))

ocr_token= ["invoice", "500"]
ocr_token2 = ocr_token 
print(id(ocr_token)) 
print(id(ocr_token2)) 

#equality vs identity
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2) 
print(id(list1) ==id(list2)) 