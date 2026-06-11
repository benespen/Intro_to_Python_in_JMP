# Logical operators

#There is no dedicated operator
#in Xor, Nand, Nor, or Xnor. You'll have to find those values
#through a combination of And, Or, and Not.
a = False
b = False

print("And:", a and b)
print("Or:", a or b)
print("Xor:", (a and not b) or (not a and b))
print("Nand:", not(a and b))
print("Nor:", not(a or b))
print("Xnor:", (a and b) or (not a and not b))