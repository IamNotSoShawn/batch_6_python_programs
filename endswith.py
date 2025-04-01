#Pseudo code for my version of endswith function

#Begin
#Input: Read a string and a suffix to check
#Extract the last N characters of the string (N is the length of the suffix)
#Compare the extracted substring with the suffix:
#If Equal, return True
#Otherwise, return False
#Output the result
#End

def last_word(word, ending):
    if len(ending) > len(word):  
        return False

    last_part = word[-len(ending):] 
    if last_part == ending: 
        return True
    else:
        return False
    
text = input("Enter a string: ")
last = input("Enter the suffix to check: ")

result = last_word(text, last)
print("Does it end with '" + last + "':", result)