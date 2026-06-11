# basic loops
# Trix are for kids, Loops are for everyone

# For loops

# the in range() construction goes from the initial index to one less than
# the final index
for i in range(1, 10):
    print(i)
    
print("First loop:")
for i in range(1,11):
    print(i)
#Write a loop here that prints the numbers from 1 to 10,
#inclusive (meaning that it prints both 1 and 10, and all
#the numbers in between). Print each number on a separate
#line.


print("Second loop:")
for i in range(-5,6):
    print(i)
#Write a loop here that prints the numbers from -5 to 5,
#inclusive. Print each number on a separate line.


print("Third loop:")
for i in range(2,21,2):
    print(i)
#Write a loop here that prints the even numbers only from 1
#to 20, inclusive. Print each number on a separate line.
#
#Hint: There are two ways to do this. You can use the syntax
#for the range() function shown in the multiple-choice
#problem above, or you can use a conditional with a modulus
#operator to determine whether or not to print.


#The other way, though, is to check to see if each
#number in a more typical range is even, and only print
#it if it is:

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
   
# if you supply a list to a for loop it will iterate over all items in the list 
grades = [100, 95, 93, 91, 90, 89, 87, 87, 85, 85, 84, 82]
sum = 0
count = 0
for grade in grades:
    count = count + 1
    sum = sum + grade
    print("Current sum:", sum)
print(sum / count)   

# you can also loop through the characters in a string
#Create letterCount and set it equal to 0
letterCount = 0 
#Run this code for each letter in the string
for character in "Hello, world": 
    #Add one to letterCount
    letterCount += 1    
print(letterCount)  

# While loops
a_num = 8

# set condition
num_digits = 0

# create while loop
while num_digits < 7:
    a_num *= 2
    num_digits = len(str(a_num))
print(a_num)