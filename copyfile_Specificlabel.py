import os
import shutil
# Folder Path
path = "/home/rohit/Documents/labels"
search_keywords = ['two-wheelers']

# Change the directory
os.chdir(path)

# Read text File
def read_text_file(file_path):
    dirPath = "/home/rohit/Documents/spilt"
    filename = file_path.split('/')[-1]
    with open(file_path, 'r') as f:
        for word in search_keywords:
            if word in f.read():
                print(filename)
                shutil.copy(file_path, dirPath)

        # print(f.read())


# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}/{file}"

		# call read text file function
		read_text_file(file_path)