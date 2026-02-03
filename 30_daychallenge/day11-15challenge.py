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


def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password
 
length = int(input("Enter the number of the length of your desired password: "))
password = generate_password(length)
print(f"Generated Password: {password}")

    
## file system, file organizer script

import os
import shutil
 

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".csv", ".json", ".xml"],
    "Others": []
}


def organize_files(directory):
    """Organizes files in the given directory by their file types."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    
 # Create folders for each category if not exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to corresponding folder
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(
                    directory, category, filename))
                file_moved = True
                break

        # Move to "Others" if no match
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))

    print(f"Files in '{directory}' have been organized successfully!")


# Example usage
directory_to_organize = input("Enter the directory path to organize: ")
organize_files(directory_to_organize)