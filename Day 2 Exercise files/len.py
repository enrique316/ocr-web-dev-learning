"""
CHAPTER 1: What Does Length Count
Objective
Understand what len() counts in a simple string.
Tasks
Store your first name
Print its length
Store your last name
Print its length
Store your full name
Print its length
Compare all three results carefully """
name = "shubhankar"
print(len(name))
last_name = "biswas"
print(len(last_name))
print(name+" "+last_name)
print(len(name + "" + last_name))
"""---------"""
me = "hi"
you = "bye"
print(me+ " "+you)

"""CHAPTER 2: Spaces and Special Characters
Objective
Understand that spaces and symbols are counted.
Tasks
Store a sentence that includes:
• Spaces
• A comma
• A full stop
Print the sentence
Print its length
Manually count characters
Compare with Python result"""

sentence = "i, am done."
print(sentence)
print(len(sentence))

"""CHAPTER 3: Empty Containers
Objective
Understand how length behaves on empty values.
Tasks
Create:
• An empty string
• An empty list
• An empty dictionary
Print the length of each
Observe the result"""
string = ""
empty_list = []
dictionary = {}
print(len(string),len(empty_list), len(dictionary))

"""CHAPTER 4: Number Illusion
Objective
Understand why integers cannot be measured directly.
Tasks
Store a 5 digit number without quotes
Attempt to check its length
Fix the issue properly
Print the correct digit count
Explain what changed"""

numbers = 12345 


"""CHAPTER 5: List Size Tracking
Objective
Understand how len() counts list items.
Tasks
Create a list with 4 items
Print its length
Add 2 more items
Print the new length
Observe the change"""

"""CHAPTER 6: Dictionary Size Logic
Objective
Understand how dictionary length works.
Tasks
Create a dictionary with 3 key value pairs
Print its length
Add one more pair
Print the length again
Identify what is being counted"""

"""CHAPTER 7: Mixed Data Container
Objective
Understand that list length counts top level items only.
Tasks
Create a list containing:
• 2 numbers
• 2 strings
• 1 list inside
Print the length
Observe carefully what is counted"""

"""CHAPTER 8: Password Validation System
Objective
Use len() inside a condition.
Tasks
Ask user to enter password
If length is less than 8 → print Weak
Otherwise → print Strong
Test with different inputs"""

"""CHAPTER 9: OCR Invoice Length Validation
Objective
Simulate real document validation logic.
Tasks
Store an invoice ID
Rule: It must be exactly 10 characters
Check its length
Print Valid or Invalid
Modify invoice ID
Test again"""

"""CHAPTER 10: Length Comparison Report
Objective
Compare length across multiple data types.
Tasks
Create:
• One string
• One list
• One dictionary
Print each value
Print each length
Write a short conclusion:
-------------------------------
What does len() count in:
String
List
Dictionary
Why does it fail on integers? """