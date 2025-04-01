#Pseudo code for my version of lower function

#Begin
#Input: Read a string
#Initialize an empty result string
#Loop through each character in the string:
#a. If character is uppercase ('A' to 'Z'), convert to lowercase by adding 32 to its ASCII value
#b. Otherwise, keep the character unchanged
#Output the new string
#End

def mylower(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z': 
#Adding 32 to the ascii value of the invidual letters turns them into their capital counterpart
            result += chr(ord(c) + 32)  
        else:
            result += c  
    return result

#Function usage
userinput = input("Enter a string: ")
print(mylower(userinput))