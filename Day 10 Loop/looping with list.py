"""
What is a List Loop?

👉 A list loop means using a loop to process every item inside a list.

A list can store:

Numbers
Strings
Mixed data
OCR fields
API data
Real Meaning

Suppose you have a list:

fruits = ["Apple", "Mango", "Orange"]

Instead of:

print(fruits[0])
print(fruits[1])
print(fruits[2])

we can use a loop:

for fruit in fruits:
    print(fruit)

Python automatically processes each item one by one.

2. First Example
Code
numbers = [10, 20, 30]

for number in numbers:
    print(number)
Output
10
20
30
"""
"""
fruit = ["mango", "organge", "pinapple", "peach"]
for x in fruit:
    print(x)

numbers = [1,2,3,4,5]
for y in numbers:
    print(y) """

# calculating totals from list numbers #
""""
a = [100, 200, 400, 700]
b = 0
for c in a:
    b += c

print(b)
"""
"""
extracted_data = [ 20, 40, 100, 50]
total = 0 
for v in extracted_data:
    total += v

print(total) """

values = [500, 100, 0.2]
total = 0 
for x in values:
    total += x

print(total)