# password strength checker 
# logic
# get an input from the user off a password
# we want to check if its strong based on the types of charaters, strongest would include lowercase letters, uppercase, numbers and special characters eg:a7?

import string
import re 
import random 

string.ascii_lowercase  # contains all the lowercase letters
string.ascii_letters
string.digits
string.punctuation 

def password_validation(password):
    
        
        if len(password) < 12:
            return False
        if not re.search(r'[A-Z]', password): # check is password contains atleast one uppercase letter
            return False
            
        if not re.search(r'[a-z]', password): # check is password contains atleast one lowercase letter
            return False
        if not re.search(r'[\d]', password): # check is password contains atleast one uppercase letter
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): # check is password contains atleast one uppercase letter
            return False
        
            
        return True

password = input("Create a password from 12-16 characters: ")
password_validation(password)

is_valid = password_validation(password)

if is_valid:
    print("Valid Password.")
else:
    print("Password does not meet requirements.")

# passowrd generator
# create a password with 12-16 characters


def password_gen():
    letters = string.ascii_letters
    digits = string.digits
    punct = string.punctuation 
    print(letters) 
    
password_gen()   
    
    
    
    

    


## file system 