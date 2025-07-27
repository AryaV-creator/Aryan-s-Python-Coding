# Python program to check the validity of a password (input from users)
import re
p=input("What password do you want to check: ")
def valid_password(p):
    if (len(p)<8 or len(p)>9):		# Fill in a number after the < and after the >
        return False			# How long should your password be?
    if not re.search ("[a-z]",p):		# Fill in a range of characters you should use
        return False			
    if not re.search ("[123456789]",p):		# Fill in a range of characters you should use between []
        return False
    if not re.search ("[A-Z]",p):		# Fill in a range of characters you should use between []
        return False
    if not re.search ("[!@#$%]",p):		# Fill in a list of characters you should use between []
        return False
    if re.search ("\s",p):			# This is telling the code there should not be any spaces 
        return False
    return True
if valid_password(p):  
    print("Valid password")  
else:  
    print("Invalid password") 

