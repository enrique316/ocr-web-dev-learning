#= assignment operator in python# 

integer = 5
string = "5"
float = 5.0
list = [1,2,3,4,5]
tuple = (1,2,3) 
set = {1,2,3,4,5} 

x = y = 5 
print(x, y)

# += in python # 
x += 5
print(x)

y = 10
y+=3
print(y)

# with strings #
name = "hello"
name += " world"
print(name)


first_name = "rohit"
first_name = "rao"
first_name += " sharma"
print(first_name)

extract_value = 5000
extract_value += 810 
print(extract_value) 

#with list [] #
list1 = [1,2,3]
list1 += [4,5,6]
print(list1)

#with tuple ()
tuple1 = (1,2,3)
tuple1 += (4,5,6)
print(tuple1)

#with sets {}

#sets={1,2,3.1}
#sets += {4,5,6} 
#print(sets)# 
# shows error while printing # 


a = [1,2]
b = a 
a += [3,4]
print(b)


# with more examples # 

a = [1,2,3]
b = a 
c = a 
a +=[4,5,6] 
print(b)
print(c) 

