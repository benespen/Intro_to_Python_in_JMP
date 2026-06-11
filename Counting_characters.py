# Counting characters

a_string = "F12dav^f%$25d"

# Initialize counter
total = 0

for a_character in a_string:
    if a_character in "0123456789":
        total += int(a_character)

print(total)