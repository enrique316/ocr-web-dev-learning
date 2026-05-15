"""
1. What is dictionary comprehension?

👉 Dictionary comprehension is a short and powerful way to:

“Create dictionaries dynamically using loops”

👉 Instead of writing:

d = {}

for x in range(5):
    d[x] = x * x

we can write everything in ONE line.

2. Basic syntax
{key:value for item in iterable}
3. Basic example
d = {x:x*x for x in range(5)}

print(d)

👉 Output:

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
4. Step-by-step breakdown
Full code
{x:x*x for x in range(5)}
Understanding each part
range(5)

Produces:

0
1
2
3
4
for x in range(5)

Loop runs one value at a time.

First iteration
x = 0

Creates:

0 : 0*0

👉 Result:

0:0
Second iteration
x = 1

Creates:

1:1
Third iteration
x = 2

Creates:

2:4

👉 Continues automatically.

Final dictionary
{
    0:0,
    1:1,
    2:4,
    3:9,
    4:16
}
5. Visual understanding
x → x*x
---------
0 → 0
1 → 1
2 → 4
3 → 9
4 → 16
6. Why comprehension is powerful

👉 It combines:

loop
dictionary creation
logic

into ONE compact structure.

7. Normal loop vs comprehension
Normal loop
d = {}

for x in range(5):
    d[x] = x*x

print(d)
Dictionary comprehension
d = {x:x*x for x in range(5)}

print(d)

👉 Same output.

But comprehension is shorter.

8. Using strings
d = {x:len(x) for x in ['cat', 'dog', 'elephant']}

print(d)

👉 Output:

{'cat': 3, 'dog': 3, 'elephant': 8}
9. Using conditions
d = {x:x*x for x in range(10) if x % 2 == 0}

print(d)

👉 Output:

{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
Why only even numbers?

Because condition:

if x % 2 == 0

filters odd numbers.

10. Internal behavior

When Python runs:

{x:x*x for x in range(5)}

it internally:

Creates empty dictionary
Starts loop
Generates key-value pair each iteration
Adds pair into dictionary
Returns final dictionary
11. Real OCR Example (important)

Suppose OCR extracted fields list.

fields = ['invoice_no', 'date', 'total']
Initialize all fields dynamically
invoice = {field:'' for field in fields}

print(invoice)

👉 Output:

{'invoice_no': '', 'date': '', 'total': ''}

👉 Very common in OCR systems.

12. Real-world examples
Student marks
marks = {
    student:0
    for student in ['A', 'B', 'C']
}

print(marks)
API response formatting
data = {
    x.upper():x
    for x in ['ok', 'fail']
}

print(data)
13. Important beginner confusion
This is dictionary comprehension
{x:x*x for x in range(5)}
This is set comprehension
{x*x for x in range(5)}

👉 Missing colon : changes structure completely.

14. Memory and performance benefit

👉 Dictionary comprehensions are usually:

faster
cleaner
more readable

than manual loops.

15. OCR Validation Example

Suppose required OCR fields:

required = ['invoice_no', 'date', 'total']
Create validation dictionary
status = {field:'missing' for field in required}

print(status)

👉 Output:

{'invoice_no': 'missing', 'date': 'missing', 'total': 'missing'}
"""