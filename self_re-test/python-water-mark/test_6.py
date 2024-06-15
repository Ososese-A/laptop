import pillow_heif
from PIL import Image

file = pillow_heif.read_heif(
    "./ye.HEIC"
)

image = Image.frombytes(
    file.mode,
    file.size,
    file.data,
    "raw"
)

image.save("./res.png", format("png"))