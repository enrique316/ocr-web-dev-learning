#String Concatenation #
name = "shubhankar"
last_name = "biswas"
print(name +" "+ last_name) 

# if we only do + ? #
my_name = "shubhankar"
my_last_n = "biswas"
print(my_name + my_last_n)
 # or we cant also do #

name1 = "john"
last1 = "wick"
movie_name = name1 +" "+ last1 
print(movie_name)

#Multiple String Concatenation #
book1 = "games of lies"
book2 = "games of truth"
book3 = "who gave a game"
print(book1 + " " + book2 + " " + book3 )

# another example #

b = "a"
c = "b"
a = "c"
d = b + " " + c + " " + a 
print(d)


#Concatenation with Variables #

no = "yes"
yes = "no"
print(no + " maybe " + yes) 

# important note #
""" concatenation only works with strings, it doesn't work with float """
#try an example #
"""
ac = 100
name = "samsung"
print( ac + " " + name)
""" 
#but you can still print with string conversion method # 
ac = 100
name = "samsung"
print(str(ac) + " " + name)


# OCR based examples #
invoice_no = 'INV2351'
amount = '500'
currency = 'USD'
print( 'invoice:' + invoice_no +' amount: '+ amount+ ' currency:'+ currency )

#lets try another example # 

invoice_h = "HG345tR"
amount_h = "7000"
currency_h = "₹Rupees"
print("invoice:"+ invoice_h + " Amount: " + amount +" Currency:" + currency_h )