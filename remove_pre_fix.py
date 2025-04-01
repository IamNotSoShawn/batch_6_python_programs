#Pseudo code for my version of removeprefix 

#Begin
#Input: Read a string and a prefix to remove
#Check if the string starts with the prefix
#If yes, extract the substring after the prefix
#If no, keep the string as it is
#Output the modified string
#End

def custom_removeprefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

text = input("Enter a string: ")
prefix = input("Enter a prefix to remove: ")
print(f"Modified: '{custom_removeprefix(text, prefix)}'")
