#String Splitting split() #
value = " name,address,phone"
print(value.split(","))

# another example #
value_1 = " One, two, three, 4 "
filtered_data = value_1.split(",")
print(filtered_data)

# example 2 # 
value_2 = " go, goa, gone "
data = value_2.split(",")
print(data)

# Using different seperator signs : and \n #
text = " One : Two : Three"
print(text.split(":"))

next1 = "hi\n i am \nshubhankar"
print(next1.split("\n"))

# accessing indexed data # 
data_1 = "IND:345"
pick_data = data_1.split(":")
print(pick_data[1])