import os
import glob

def delete_files(folder_path, file_extension):
    files = glob.glob(f"{folder_path}/*{file_extension}")
    for file in files:
        try:
            os.remove(file)
            print(f"File {file} has been deleted successfully")
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")
