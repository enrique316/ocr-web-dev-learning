# what is nested function #
def name():
    def last_name():
        print("Biswas")
    
    last_name()



name()

   
# another example #

def a():
 def b():
    print("hi")

    b()

    
a()