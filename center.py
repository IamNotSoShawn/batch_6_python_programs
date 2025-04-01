#Pseudo code for my version of center function 

#Begin
#Input: Read a string and the desired width
#calculate the number of spaces required on each side
#a. Left side = (width - length of string) divided by 2
#b. Right side = (width - length of string) - Left side 
#Concatenate spaces on both sides
#Output the centered string
#End

def center_text(word, total_width):
    if len(word) >= total_width:  
        return word
    
    extra_spaces = total_width - len(word)  
    left_side = extra_spaces // 2  
    right_side= extra_spaces - left_side
    
    centered_word = " " * left_side + word + " " * right_side
    return centered_word  

