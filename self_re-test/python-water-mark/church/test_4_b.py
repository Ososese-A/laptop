from test_4 import mark_image
import os

def finalizing (folder_path):
    files_list = os.listdir(folder_path)

    for your_file_name in files_list:
        if '.png' in your_file_name:
            print(your_file_name)
            print(f"res_{your_file_name[:-4]}")
            mark_image(your_file_name , f"res_{your_file_name[:-4]}.png", "water.png")
        if '.jpg' in your_file_name:
            print(your_file_name)
            print(f"res_{your_file_name[:-4]}")
            mark_image(your_file_name , f"res_{your_file_name[:-4]}.png", "water.png")