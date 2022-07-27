# Move Files by count
# import os
# import random
# import shutil

# source = "/home/rohit/Documents/DetracCombined/images"
# destination = "/home/rohit/Documents/DetracCombined/val/images"

# os.chdir(source)

# count =0

# while count < 27651:
#     random_filename = random.choice(os.listdir(source)) 
#     shutil.move(source+"/"+random_filename, destination)
#     print(source , random_filename)
#     count += 1


# Compare and move files by count

import os
import shutil
# Folder Path
label_path = "/home/rohit/Documents/DetracCombined/labels"


# Change the directory
os.chdir(label_path)

# Read text File
def copyImage(file_path):
    image_dirPath = "/home/rohit/Documents/DetracCombined/val/images"
    filename = file_path.split('/')[-1]
    imageName = filename.split('.')[0]
    # print(filename)
    for file in os.listdir(image_dirPath):
        if file.endswith(".png"):
            file_path = f"{label_path}/{file}"
            # print(file_path)
            labelPath= file_path.split('/')[-1]
            labelName = labelPath.split('.')[0]
            # print(labelName)
            compare(labelName, imageName)

# # Compare
def compare(labelName, imageName):
    compared_imagePath = "/home/rohit/Documents/DetracCombined/val/labels"
    
    if not os.path.exists(compared_imagePath):
        os.makedirs(compared_imagePath)
    
    if os.path.exists(compared_imagePath):
        if imageName == labelName:
            # print("File:",file_path)
            # print("Compared:",compared_imagePath)
            print("IMAGE:",imageName)
            print("LABEL:",labelName)
            shutil.move(file_path, compared_imagePath)

# iterate through all file
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{label_path}/{file}"
        copyImage(file_path)
        # print(file_path)