#importing the os module
import os

#specifying the path of the diectory
dir_path="/Users/gauravsh/Desktop/python"

#listing the files and directories in the specified path
items=os.listdir(dir_path)

#printing the names of the files and directories
for item in items:
    print(item)
    