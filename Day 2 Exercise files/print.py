# print funcation in python # 

name = "shubhankar"
age = 21
city = "rewari"

if name == "shubhankar":
   print( " name is valid")

else:
    print(" name is invalid")

"""practice chapter
CHAPTER 1: Basic Output Confidence

Objective
Understand how print displays values.

Tasks

Print your name

Print your city

Print a number like 100

Print a decimal number like 45.67

Print True

Goal
Understand that print can display different types directly.

"""

name = "Diti"
City = "rewari"
number = 100
decimal_number = 45.67 

extracted_data = 100
actual_data = 50 

if extracted_data > actual_data:
    print("true")
else:
    print("false")


"""
CHAPTER 2: Multiple Values in One Print

Objective
Understand how comma separation works.

Tasks

Print your name and age in one line using comma

Print three numbers together

Print a word and a number together

Observe
Notice how Python automatically adds space between comma separated values.

"""
name = "shubhankar"
age = 37
print(name, age)

number = 1
number2 = 3
number3 = 7
print( number, number2, number3) 

word = "hello"
x = 7 
print( word, x, sep=",") 

number = 1
number2 = 3
number3 = 7
print( number, number2, number3, sep=":") 


number = 1
number2 = 3
number3 = 7
print( number, number2, number3, sep="/") 

"""
CHAPTER 3: Using Variables with print()

Objective
Print stored data.

Tasks

Create variable name = "Ravi"

Create variable amount = 5000

Print both in one line

Change amount to 7000 and print again

Goal
Understand that print shows current stored value.

"""
name = "Ravi"
amount = 5000
print(name, amount)
amount = 7000
print(name, amount)


"""
CHAPTER 4: Custom Separator

Objective
Control spacing using sep.

Tasks

Print "Invoice", "2026", "Paid" separated by dash

Print numbers separated by colon

Print three words separated by slash

You must use:
sep= """

name = "invoice"
number = 2026
status = "paid"
print( name, number, status, sep=":")
print(name, number, status, sep="/")
print( name, number, status, sep="-")




"""CHAPTER 5: Custom Line Ending

Objective
Control how print ends.

Tasks

Print "Hello" without moving to next line

Print another word after it

Experiment using end=" "

Experiment using end="-"

"""
print("hello", end="")
print("world", end="-")

"""CHAPTER 6: Printing Quotes Inside Text

Objective
Handle string formatting inside print.

Tasks

Print: Ravi said "Invoice paid"

Print: It's completed

Try both single and double quotes properly """

print("ravi said \"invoice paid\"")
print("its completed")
print('it\'s completed') 

"""CHAPTER 7: Simple Formatting Style

Objective
Make output look structured.

Tasks

Print:
Name: Ravi
Amount: 5000
Status: Paid

Make it look clean and aligned """
name = "ravi"
amount = 5000
status = "paid" 
print(name, amount, status, sep="\n")




"""CHAPTER 8: OCR Style Raw Output Simulation

Objective
Simulate messy OCR output display.

Tasks

Print:
" 7800 "

Print:
"Invoice No: 4567 "

Print:
"Status: PAID "

Goal
Understand how raw data appears before cleaning. """
print("7800")
print("invoice no:4567")
print("status:paid")

"""CHAPTER 9: Print Debugging Practice

Objective
Use print for debugging.

Tasks

Create variable amount = 4500

Print: "Amount before tax:", amount

Calculate tax = amount * 0.18

Print: "Tax calculated:", tax

Print: "Final amount:", amount + tax

Goal
See how print helps track logic. """

amount = 4500
print("amount before tax", amount)
tax = amount * 0.18 
print("tax calculated:", tax)
print("final amount:", amount + tax)

"""CHAPTER 10: Mini Structured Report

Objective
Create a small console report using only print.

Make output look like:

----- Invoice Report -----
Customer: Ravi
Amount: 7800
Tax: 1404
Total: 9204
Status: Paid

Only use print.
No new concepts.
""" 