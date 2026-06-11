# Dictionaries

story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

#In Bryan Cranston's autobiography, he describes how after
#his success on Breaking Bad, he developed a scoring system
#for evaluating new scripts that he received.
#
#First, he would assign the script a grade -- A, B, C, D, or
#F -- in each of five categories: Story, Text, Role, Director,
#and Cast.
#
#Then, he would tally those grades into a total score for the
#script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
#For example: an A story, B text, C role, D directory, and
#F cast would get a score of 12: +6 for the story, +4 for the
#text, +2 for the role, +0 for the director, and +0 for the
#cast.
#
#Then, based on that score, the script would be assigned a
#category (note these are slightly different from the image
#because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
#The variables above give the letter grades assigned to each
#of the five components. Write a program that calculates the
#total score he would assign to the script represented by
#these variables. Then on the next line, print the category
#he would assign to that script. For example, for the values
#above, this program would print:
#
#12
#On the bubble

# Dictionaries are a way for us to
#easily store how many points correspond to each letter
#grade even though they differ from category to category.

#First, we want to create the dictionaries that store these
#scores:

story_dict = {"A": 6, "B": 5, "C": 4, "D": 2, "F": 0}
text_dict = {"A": 5, "B": 4, "C": 3, "D": 1, "F": 0}
role_dict = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
director_dict = {"A": 3, "B": 2, "C": 1, "D": 0, "F": 0}
cast_dict = {"A": 2, "B": 1, "C": 0, "D": 0, "F": 0}

#In story_dict, 6 is associated with "A", so the right
#number of points are assigned to an "A" story, and that
#differs from the points assigned to "A" in text_dict.
#
#From here, calculating our total_score is straightforward:

total_score = 0
total_score += story_dict[story]
total_score += text_dict[text]
total_score += role_dict[role]
total_score += director_dict[director]
total_score += cast_dict[cast]
print(total_score)

#This syntax says, "Find
#the value associated with story in story_dict." The value
#associated with "A" in story_dict is 6, so 6 is added.
#
#There really is no easier way to do the last part, though:
if total_score >= 20:
    print("Perfect score")
elif total_score >=17:
    print("Must do")
elif total_score >= 14:
    print("Seriously consider")
elif total_score >= 12:
    print("On the bubble")
else:
    print("Pass")