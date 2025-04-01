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


def custom_lstrip(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    return s[i:]
