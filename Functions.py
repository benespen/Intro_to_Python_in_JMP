#functions

# A function called total_volume. total_volume should
#have four parameters, all integers. The first three
#parameters should represent the length, width, and height
#of a box respectively. The fourth should represent the
#number of boxes.
#
#The function should return an integer representing the
#total volume represented by the given boxes. For example,
#if the length is 10, the width is 2, the height is 2, and
#there are 4 boxes, then the total volume would be 160:
#((10 * 2 * 2) * 4) = 160.

def total_volume(length, width, height, number_of_boxes):
    vol = length * width * height * number_of_boxes
    return(vol)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 160
test_length = 10
test_width = 2
test_height = 2
test_box_count = 4
result = total_volume(test_length, test_width, test_height, test_box_count)
print(result)

#A function called what_season. what_season should
#have two parameters: the first a string representing
#a month, and the second an integer representing a day.
#
#what_season should return "Spring" if the date is in
#Spring, "Summer" if it's in Summer, "Fall" if it's in
#Fall, and "Winter" if it's in Winter.
#
#For this problem, we define those seasons as follows:
#
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
#
#So, March 20 to June 20 would be Spring; June 21 to
#September 21 would be Summer; September 22 to December
#20 would be Fall; and December 21 to March 19 would be
#Winter.

def what_season(month, day):
    if month == 'March':
        if day < 20:
            return 'Winter'
        else:
            return 'Spring'
    elif month == 'April': 
        return 'Spring'
    elif month == 'May':
        return 'Spring'
    elif month == 'June':
        if day < 21:
            return 'Spring'
        else:
            return 'Summer'
    elif month == 'July':
        return 'Summer'
    elif month == 'August':
        return 'Summer'
    elif month == 'September':
        if day < 22:
            return 'Summer'
        else:
            return 'Fall'
    elif month == 'October':
        return 'Fall'
    elif month == 'November':
        return 'Fall'
    elif month == 'December':
        if day < 21:
            return 'Fall'
        else:
            return 'Winter'
    elif month == 'January':
        return 'Winter'
    elif month == 'February':
        return 'Winter'
    else:
        return None
       
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 15))
print(what_season("June", 23))
print(what_season("September", 27))

#Consult this blood pressures chart: http://bit.ly/2CloACs
#
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).


def check_blood_pressure(SBP,DBP):
    if SBP < 90 and DBP < 60:
        return 'Low'
    elif SBP < 120 and DBP < 80:
        return 'Ideal'    
    elif SBP < 140 and DBP < 90:
        return 'Pre-high'
    else:
        return 'High'

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Ideal
test_systolic = 110
test_diastolic = 60

print(check_blood_pressure(test_systolic, test_diastolic))

# Pokemon damage

#Your function for calculate_damage must call calculate_modifier;
#it may not calculate the modifier separately. As such,
#calculate_damage should accept all ten parameters: STAB,
#Type, Critical, Other, Random, Level, Attack, Defense, and
#Base. You'll need to pass STAB, Type, Critical, Other, and
#Random to calculate_modifier.
#
#Make sure the parameters to each function follow the order
#shown above.
#
#As a reminder, damage is calculated using this formula:
#courses.edx.org/asset-v1:GTx+CS1301xII+1T2018+type@asset+block@DamageCalc.png
#
#Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png


#Add your code here!
def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    level_modifier = (2 * Level + 10) / 250
    return (level_modifier * (Attack/Defense) * Base + 2) * modifier

def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB * Type * Critical * Other * Random


#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16.0
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))

#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.

#First, let's start with letter count. There are a few ways
#we could implement letter count, but because we know our
#string is only spaces and letters, we can do this an easy
#way.
#
#First, we create the function:
def letter_count(a_string):
    
    #Then, start the counter:
    letters = 0
    
    #Then, we loop through each letter in the function:
    for character in a_string:
        
        #If it's not a space, then it must be a letter!
        if not character == " ":
            letters += 1
            
    #Finally, we return how many letters we found.
    return letters

#word_count is the exact opposite. Instead of counting the
#characters that are not spaces, we only want to count the
#spaces:
def word_count(a_string):
    
    #Here, we'll initialize our initial count to 1 because
    #each space starts a new word -- that means we have one
    #word to begin with.
    words = 1
    
    #Now, same loop:
    for character in a_string:
        
        #But opposite condition:
        if character == " ":
            words += 1
            
    return words

#With those two functions, our word length function is simple.
#We divide the results of letter_count by the results of
#word_count.
def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)
    
a_string = "Up with the white and gold"
print(letter_count(a_string))
print(average_word_length(a_string))