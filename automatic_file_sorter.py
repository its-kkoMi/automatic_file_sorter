# Automatic File Sorter - For common files of students like me :D
# Reference: https://www.youtube.com/watch?v=gs0FNQR0njI&ab_channel=AlexTheAnalyst

# Import os
import os, shutil

# Select path (Note: Make sure to use normal slash instead of backslash, and add an extra slash at the end)
path = r"C:/Users/James\Desktop/James\A.Y. 2023-2024/1st Sem/CMPE 102/Programs/Final Project/automatic_file_sorter/"

# Show the files in the path
file_name = os.listdir(path)

print(os.listdir(path)) # This let me see the files in the path (Not Required)

# List of folder names
folder_names = ['Excel Files', 'Image Files', 'Text Files', 'Doc Files', 'PDF Files', 'PPT Files', 'Video Files', 'Audio Files']



# Check if the path has the folders, if not, then create folders

number_of_folder_names = len(folder_names) # Counts how many types of files are in the list

for loop in range(0, number_of_folder_names):
    if not os.path.exists(path + folder_names[loop]): # Checks if folder exists in path
        os.makedirs(path + folder_names[loop])        # Creates new folder in path
        
# Check and move the files to their corresponding folders    