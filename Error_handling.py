# Error handling

mystery_value = "True"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and 
#prints the result. In the case that mystery_value is 
#equal to 0, print "Can't divide by zero". If for any other
#reason the operation fails, print "Not possible".

try:
    print( 10 / mystery_value )
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Not possible")
    
def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as error:
        return error


#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#invalid literal for int() with base 10: 'Boggle.'
#5
print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))