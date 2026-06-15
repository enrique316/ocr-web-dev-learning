"""
1. What is the range() Function?

👉 The range() function generates a sequence of numbers.

It is commonly used with a for loop when you want to repeat something a specific number of times.

Real Meaning

Suppose you want to print:

0
1
2
3
4

Instead of manually creating a list:

for i in [0, 1, 2, 3, 4]:
    print(i)

Python can generate these numbers automatically:

for i in range(5):
    print(i)
2. First Example
for i in range(5):
    print(i)
Output
0
1
2
3
4
Why Not 5?

Many beginners expect:

0
1
2
3
4
5

But range(5) means:

Start at 0
Stop BEFORE 5

So Python generates:

0
1
2
3
4
"""
"""
for x in range(5):
    print(x)


for z in range(20):
    print(z)

# specific range #
for y in range(3, 4):
    print(y)

# using step values #
for a in range (1, 3, 2):
    print(a)
"""
"""
for b in range(2, 10, 5):
    print(b)
"""
"""
for x in range(4, 7, 3):
    print(x)
"""
"""
for y in range (2, 11, 7):
    print(y)

for ab in range (0, 4, 1):
    print(ab)
"""

# negative range #

for cd in range(0, 10, -3):
    print(cd)