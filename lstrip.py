#Pseudo code for my version of lstrip

#Begin
#Input: Read a string from the user
#Initialize an empty result string
#Initialize a flag found_non_space as False
#Loop through each character in the string:
#a. If the character is NOT a space, set found_non_space to True
#b. If found_non_space is True, add the character to the result string
#Output the result string
#End 


def remove_leading_spaces(s):
    result = ""
    found_char = False
    for char in s:
        if char != " " or found_char:
            result += char
            found_char = True
    return result