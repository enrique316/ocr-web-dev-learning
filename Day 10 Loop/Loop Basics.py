"""
1. What is a For Loop?

👉 A for loop is used when you want to repeat something for every item inside a collection.

A collection can be:

List
String
Tuple
Set
Dictionary
Real Meaning

Suppose you have 5 OCR fields:

field1
field2
field3
field4
field5

Without a loop:

print(field1)
print(field2)
print(field3)
print(field4)
print(field5)

This becomes repetitive.

A for loop automates the repetition.

Basic Example
for i in [1, 2, 3]:
    print(i)
Output
1
2
3
2. Understanding the Structure
Syntax
for variable in sequence:
    code
Example
for i in [1, 2, 3]:
    print(i)
Parts
Part 1
for

Starts the loop.

Part 2
i

Temporary variable.

Stores one item at a time.

Part 3
in

Means:

Take items from
Part 4
[1, 2, 3]

The sequence being processed.

Part 5
print(i)

Runs for every item.
"""
names = ["john", "tine", "jim", "britney"]
for names in names:
    print(names)

extracted_invoice_values = (10, 4000, 50000, 343.3)
for extracted_invoice_values in extracted_invoice_values:
    print(extracted_invoice_values)
for names in ["john", "tine", "jim", "britney"]:
    print(names)