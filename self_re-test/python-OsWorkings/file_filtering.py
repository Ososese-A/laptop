import os

# your_folder_path = r'D:\sample'
your_folder_path = r'C:\\Users\\akhid\\Pictures\\MUAH'

list_of_files = os.listdir(your_folder_path)

for your_file_name in list_of_files:
    print(your_file_name)

for your_file_name in list_of_files:
    if '.xlsx' in your_file_name:
        print(your_file_name)

for root, dirs, files in os.walk(your_folder_path):
    print(str(root + " " + str(dirs) + " " + str(files)))
    print(root)