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
# Check and move the files to their corresponding folders    