#Pseudo code for my version of ljust function

#Begin
#Input: Read a string and the desired width
#Calculate the number of spaces needed (width - length of string)
#Concatenate the original string with the required spaces
#Output the justified string
#End

def left_pad(word, total_width):
    if len(word) >= total_width: 
        return word
    
    spaces_needed = total_width - len(word)  
    padded_word = word + " " * spaces_needed  
    return padded_word  

text = input("Enter a string: ")
width = int(input("Enter the desired width: "))

justified = left_pad(text, width)
print(justified )
