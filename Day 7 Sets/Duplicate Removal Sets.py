"""
1. What does this mean?

👉 It means:

👉 “Using sets to automatically remove duplicate values”

2. Why sets remove duplicates

👉 Sets only store unique values

👉 Duplicate items are ignored automatically

3. Basic example
s = {1, 1, 2, 3, 3}

print(s)


"""
a = {1,2,3,4,5,5,5,5}
print(a)

# clean data from list using set method # 

b = [1,2,3,4,4,4,4]
clean = set(b)
print(clean)