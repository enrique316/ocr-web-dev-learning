# append .append() # 
"""
1. What is append()?
append() means:
👉 Adding a new item to a list
👉 Always adds at the end

It modifies the original list """ 

x = [1]
x.append(2)
print(x)

# another example with string #
names = ["Ram", "Shyam", "Sita",]
names.append("gita")
print(names)

# try adding multiple values # 
"""names_list = ["Jack", "Rose"]
names.append("james", "paula")
print(names)""" # this method dont work#

names_list = ["Jack", "rose"]
names.append("James")
names.append("paula")
print(names)

# appending list # 

new_list = [1,2,3,4]
new_list.append(5)
print(new_list)

y = [3,4,5,6]
y.append([7,8])
print(y)

