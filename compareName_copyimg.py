import os
import shutil
# Folder Path
path = "/home/rohit/Documents/images"

# Change the directory
os.chdir(path)

# Read text File
def copyImage(file_path):
    dirPath = "/home/rohit/Documents/spilt"
    filename = file_path.split('/')[-1]
    imageName = filename.split('.')[0]
    # print(imageName)
    for file in os.listdir(dirPath):
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            # print(file_path)
            labelPath= file_path.split('/')[-1]
            labelName = labelPath.split('.')[0]
            # print(labelName)
            compare(labelName, imageName)

# Compare
def compare(labelName, imageName):
    imagePath = "/home/rohit/Documents/split_images"
    if labelName == imageName:
        print(imageName)
        print(labelName)
        shutil.copy(file_path, imagePath)

# iterate through all file
for file in os.listdir():
    if file.endswith(".png"):
        file_path = f"{path}/{file}"
        copyImage(file_path)