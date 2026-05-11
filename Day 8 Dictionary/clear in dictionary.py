"""
1. What is clear()?

👉 clear() is a dictionary method used to:

“Remove ALL items from a dictionary”

👉 After using clear():

Dictionary becomes empty.

2. Basic syntax
dictionary.clear()
"""

a = {
    'name': "Shubhankar",
    'last_name': "Biswas"
}
a.clear()
print(a)

"""
| Feature                 | `clear()` | `del` |
| ----------------------- | --------- | ----- |
| Removes items           | ✅ Yes     | ✅ Yes |
| Removes variable itself | ❌ No      | ✅ Yes |
| Dictionary still usable | ✅ Yes     | ❌ No  |


"""


