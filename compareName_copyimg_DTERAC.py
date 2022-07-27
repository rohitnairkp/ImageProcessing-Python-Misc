import os
import shutil
# Folder Path
image_path = "/home/rohit/Downloads/Check-Images/Annotations_CarOnly/images/val"

# Change the directory
os.chdir(image_path)

# Read text File
def copyImage(file_path):
    label_dirPath = "/home/rohit/Downloads/Check-Images/Annotations_CarOnly/labels/val"
    filename = file_path.split('/')[-1]
    imageName = filename.split('.')[0]
    # print(filename)
    for file in os.listdir(label_dirPath):
        if file.endswith(".txt"):
            file_path = f"{image_path}/{file}"
            # print(file_path)
            labelPath= file_path.split('/')[-1]
            labelName = labelPath.split('.')[0]
            # print(labelName)
            compare(labelName, imageName)

# # Compare
def compare(labelName, imageName):
    compared_imagePath = "/home/rohit/Downloads/Check-Images/Annotations_CarOnly/annotated_val_Images"
    
    if not os.path.exists(compared_imagePath):
        os.makedirs(compared_imagePath)
    
    if os.path.exists(compared_imagePath):
        if imageName == labelName:
            # print("File:",file_path)
            # print("Compared:",compared_imagePath)
            # print("IMAGE:",imageName)
            # print("LABEL:",labelName)
            shutil.move(file_path, compared_imagePath)

# iterate through all file
for file in os.listdir():
    if file.endswith(".jpg"):
        file_path = f"{image_path}/{file}"
        copyImage(file_path)
        # print(file_path)