# Automatic File Sorter - For common files of students like me :D
# Reference: https://www.youtube.com/watch?v=gs0FNQR0njI&ab_channel=AlexTheAnalyst

# Import os
import os, shutil

# Select path (Note: Make sure to use normal slash instead of backslash, and add an extra slash at the end)
path = r"C:/Users/James\Desktop/James\A.Y. 2023-2024/1st Sem/CMPE 102/Programs/Final Project/automatic_file_sorter/"

# Show the files in the path
file_name = os.listdir(path)

print(os.listdir(path)) # This let me see the files in the path (Optional)

# List of folder names
folder_names = ['Excel Files', 'Image Files', 'Text Files', 'Doc Files', 'PDF Files', 'PPT Files', 'Video Files', 'Audio Files']

# Check if the path has the folders, if not, then create folders
number_of_folder_names = len(folder_names) # Counts how many types of files are in the list

for loop in range(0, number_of_folder_names):
    if not os.path.exists(path + folder_names[loop]): # Checks if folder exists in path
        os.makedirs(path + folder_names[loop])        # Creates new folder in path
        print("Folder created successfully!")         # Notifies the user that it has successfully created a folder
        
# Check and move the files to their corresponding folders
for file in file_name: # Note: You can add extra "elif" for whatever type of files you have in the path, 
                       # or if you want to sort only specific files
    
    # Check and move .docx files
    if ".docx" in file and not os.path.exists(path + "Doc Files/" + file):
        shutil.move(path +  file,path + "Doc Files/" + file)
                
    # Check and move .xlsx files
    elif ".xlsx" in file and not os.path.exists(path + "Excel Files/" + file):
        shutil.move(path +  file,path + "Excel Files/" + file)

    # Checks and moves .pptx files
    elif ".pptx" in file and not os.path.exists(path + "PPT Files/" + file):
        shutil.move(path +  file,path + "PPT Files/" + file)
    
    # Check and move .pdf files
    elif ".pdf" in file and not os.path.exists(path + "PDF Files/" + file):
        shutil.move(path +  file,path + "PDF Files/" + file)
    
    # Check and move .png and .jpg files
    elif ".png" in file and not os.path.exists(path + "Image Files/" + file):
        shutil.move(path +  file,path + "Image Files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "Image Files/" + file):
        shutil.move(path +  file,path + "Image Files/" + file)
    
    # Checks and moves .mp4 files
    elif ".mp4" in file and not os.path.exists(path + "Video Files/" + file):
        shutil.move(path +  file,path + "Video Files/" + file)
        
    # Checks and moves .mp3 files
    elif ".mp3" in file and not os.path.exists(path + "Audio Files/" + file):
        shutil.move(path +  file,path + "Audio Files/" + file)
        
    # Check and move .txt files
    elif ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path +  file,path + "Text Files/" + file)

# Note: This can automatically run in the background using "Task Scheduler" in Windows or other OS