"""
1. What does this mean?
👉 It means:
👉 “Removing values from a set”
2. Methods used
👉 Two main methods:
remove()
discard()
"""

name = {"dimpal", "diti", "gauri"}
name.remove("dimpal")
# Now with .discard #
name.discard("gauri")
print(name)
# important behavior with discard # if the value isnt present, it will provide the original full existing value #  
name.discard("happy")


