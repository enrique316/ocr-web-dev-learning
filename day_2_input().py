#input() variables 
name = input("What is your name? ")

age = int(input("What is your age? "))

invoice_amount = float(input("What is the invoice amount? "))

#boolean with input()

check_value =input("is the value correct?:")
print(bool(check_value)) 

#list with input()
items_name = input("pen, pencil, eraser, ruler: ")
items_list = items_name.split(',')

#complex number with input()
assigned_value = complex(input("enter a complex number: "))


#declaring multiple variables with in one line with 
first_name, my_age, gender, country = "Shankar", '37', "male", "India"

print(first_name)
print(my_age)
print(gender)
print(country)


