#Pseudo code for my version of isupper function

#Begin
#Input: Read a string
#Loop through each character in the string:
#a. If there is at least one lowercase letter ('a' to 'z'), return False
#If no lowercase letters are found, return True
#Output the result
#End

def my_uppercase_check(text):
    for letter in text:
        if letter >= 'a' and letter <= 'z':  
            return False  
    return True 

userinput = input("Enter anything: ")
print(my_uppercase_check(userinput))
