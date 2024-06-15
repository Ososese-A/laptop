import pillow_heif
from PIL import Image
from test_8 import delete_files
import os



#to convert the files form heic to png and rename them 
# i = 10001
# for oto in heic_files:
#     graph = pillow_heif.read_heif(f"./church/{oto}")
#     image = Image.frombytes(graph.mode, graph.size, graph.data, "raw")
#     image.save(f"{i}_res.png", format("png"))
#     i += 1
#     print(i)