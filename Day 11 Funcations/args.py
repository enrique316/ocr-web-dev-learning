# what is *args in python # 
def name(*names):
    print(names)
name("ram," "shyam")

# Another example #

def count(*numbers):
    print(numbers)
count(1,2,3)

#  using sum with *args #
def total(*numbers):
    print(sum(numbers))
total(1,4,5)

#another example #
def total(*numbers):
    return (sum(numbers))
finale_result = total(20, 50, 60)
print(finale_result)

# what is we pass one value #
def identity(*names):
   print("ram", "Shyam", "Sita", "gita")
