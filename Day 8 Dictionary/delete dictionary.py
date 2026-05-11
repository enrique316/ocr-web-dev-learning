"""
1. What does deleting dictionary mean?

👉 Deleting dictionary means:

“Removing the entire dictionary variable from memory”

👉 This is different from:

clear()

because clear() only removes items.

👉 del can completely destroy the dictionary variable itself.

2. Basic syntax
del dictionary_name
"""

x = {
    'name': "Simba"
}
del x['name']
print(x)