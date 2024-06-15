import pillow_heif
from PIL import Image
from test_8 import delete_files
import os

def convert_heic_to_png(path):
    #load all the heif files into a list 
    heic_files_cap = [photo for photo in os.listdir(f"{path}") if '.HEIC' in photo]
    heic_files_low = [photo for photo in os.listdir(f"{path}") if '.heic' in photo]
    # print(heic_files)

    i = 10001
    for oto in heic_files_cap:
        try:
            graph = pillow_heif.read_heif(f"{path}/{oto}")
            image = Image.frombytes(graph.mode, graph.size, graph.data, "raw")
            image.save(f"{i}_res.png", format("png"))
            print(i)
            i += 1
        except OSError as e:
            print(f"Error: {oto} : {e.strerror}")

    for loto in heic_files_low:
        try:
            graph = pillow_heif.read_heif(f"{path}/{loto}")
            image = Image.frombytes(graph.mode, graph.size, graph.data, "raw")
            image.save(f"{i}_res.png", format("png"))
            print(i)
            i += 1
        except OSError as e:
            print(f"Error: {loto} : {e.strerror}")

    delete_files(f"{path}", '.HEIC')

convert_heic_to_png('./test_files')