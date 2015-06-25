import os

mywork_dir=r"C:\Users\Lizzy Yao\Desktop\prank\prank"

file_list = os.listdir(mywork_dir)

os.chdir(mywork_dir)

for file_name in file_list:
    os.rename(file_name, file_name.translate(None,"0123456789"))
 
