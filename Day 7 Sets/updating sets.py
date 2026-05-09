"""
1. What does this mean?
👉 It means:
👉 “Adding multiple values into a set at once”
2. Method used
👉 We use:
update()
"""

a = {7.3,5,9,2,1}
a.update([10,11])
print(a)

# ----# 
xy = {"sdasdas", 4234039, 13432423422.3242423}
xy.update({232323})
print(xy)

"""ab = {4,55,'adsads', True}
ab.update(False)
print(ab) """ # boolean isnt acceptable # 

# another example # 

abc = {2,3}
absz = {3,4}
abc.update(absz)
print(abc)

invoice_amount = {200, 500}
updated_amount = {700, 800}