"""CHAPTER 1: Basic Type Identification

Objective
Understand what type Python assigns to different values.
Tasks
Create a variable storing your name
Print its value
Print its type
Create a variable storing an integer number
Print its value
Print its type
Create a variable storing a decimal number
Print its value
Print its type
Create a boolean variable
Print its value
Print its type
Focus
Observe how Python classifies each value internally."""
name ="shubhankar"
print(name)
print(type(name))

#integer# 
extracted_value = 1000
print(extracted_value)
print(type(extracted_value))

#decimal# 
ocr_value = 12.5
print(ocr_value)
print(type(ocr_value))

password_valid = True
password_invalid = False
print(password_valid)
print(password_invalid)
x = 3
y= 4
print(type(x>4)) 



"""
CHAPTER 2: Numeric String vs Real Number

Objective
Understand that looking like a number does not mean it is a number.

Tasks

Store "5000" as a value
Print its type
Store 5000 without quotes
Print its type
Compare both types and observe the difference carefully """

value = "5000"
print(type(value))
value1 = 5000
print(type(value1))
print(type(value), type(value1))
print(type(value) == type(value1)) 

"""
CHAPTER 3: Type After Arithmetic
Objective
Understand how operations affect type.
Tasks
Create an integer variable
Multiply it by another integer
Print result type
Multiply integer by decimal
Print result type
Observe the difference. """

ocr = 78
b = 2
x = 78 * 2
print(x)
print(type(x))

extracted_value1 = 90
finale = 2.4
b = extracted_value * finale 
print(b)
print(type(b))


"""
CHAPTER 4: Mixed Addition
Objective
Understand automatic type promotion.
Tasks
Create one integer variable
Create one float variable
Add them
Print result
Print result type """

a = 10
b = 2.5
c = a + b 
print(c)
print(type(c))


"""
CHAPTER 5: Boolean Result Type
Objective
Understand comparison result type.
Tasks
Compare two numbers
Store result in a variable
Print the result
Print its type """
name = 40
age = 37
comparison = name > age
print(comparison)
print(type(comparison))

"""
CHAPTER 6: OCR Style Simulation
Objective
Understand why OCR data must be converted.
Tasks
Store an extracted amount as text
Print its type
Convert it into numeric form
Print new type
Observe the change. """
extracted_amount = "500"
print(type(extracted_amount))
converterd_value = int(extracted_amount)
print(type(converterd_value))

"""
CHAPTER 7: Multi Variable Type Report
Objective
Create a mini type inspection report.
Tasks
Create variables of:
• string
• integer
• float
• boolean
Print each value and its type clearly."""
name =  "Shubhanakr"
age = 37
weight = 84.3 
married = True
print(name)
print(type(name))
print(age)
print(type(age))
print(weight)
print(type(weight))
print(married)
print(type(married))

"or"

print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Weight:", weight, "| Type:", type(weight))
print("Married:", married, "| Type:", type(married))




"""
CHAPTER 8: Same Value Different Type

Objective
Understand value equality vs type equality.
Tasks
Store 100 as number
Store "100" as string
Compare their types
Print the result """
a = 100
b = "100"
print(type(a) == type(b))
"""
CHAPTER 9: Type of Type

Objective
Understand that type() itself has a type.

Tasks
Print type of an integer
Print type of the result you got above
Observe carefully what Python returns. """
h = 70
print(type(h))
print(type(type(h)))
"""
CHAPTER 10: Mini Type Validator

Objective
Simulate validation thinking.
Tasks
Store an age value as text
Print its type
Convert it to integer
Print new type
Check whether the variable is integer after conversion """


age = "10"
print(type(age))
x = int(age)
print(type(x))