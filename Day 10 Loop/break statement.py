"""
What is the break Statement?

👉 The break statement immediately stops a loop.

When Python encounters break:

The current loop ends immediately.
Remaining iterations are skipped.
Execution continues after the loop.
Real Meaning

Suppose you are searching for a specific invoice.

Once you find it, there is no need to continue searching.

Instead of checking every remaining item:

INV001
INV002
INV003 ← Found it
INV004
INV005

You can stop immediately using break.

First Example
for i in range(5):
    if i == 3:
        break

    print(i)
Output
0
1
2
"""