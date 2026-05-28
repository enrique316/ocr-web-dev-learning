"""
What is Short Circuit Evaluation?

👉 Short circuit means:

“Python stops checking conditions early when final answer is already known.”
Real Meaning

Python tries to save:

time
memory
processing power

by avoiding unnecessary condition checks.

Why This Is Important?

Real systems like:

OCR engines
AI pipelines
APIs
fraud detection systems

may process HUGE data.

If Python can stop early:

👉 system becomes faster.

2. Short Circuit With AND

In AND condition:

Everything must be True

So if Python finds ONE False condition:

👉 it immediately stops checking remaining conditions.

Because final answer can NEVER become True anymore.

Proper Example
a = 5
b = 10

if a > 10 and b > 5:
    print("Valid")
else:
    print("Invalid")
"""

amount = 35000
captured_amount = 35002
name = "Dinesh"
if amount < 35000 and captured_amount == 35002:
    print("true")
else:
    print("false")

# another example with different conditions #

first_amount = 350
second_amount = 355
client_name = "Naresh"
if first_amount == 358 or second_amount < 356 :
    print("true")
else:
    print("false")