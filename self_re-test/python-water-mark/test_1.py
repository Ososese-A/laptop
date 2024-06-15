from PIL import Image

def create_watermark_image(inputImage, outputImage, marker, position):
    baseImage = Image.open(inputImage)
    watermark = Image.open(marker)

    baseImage.paste(watermark, position, mask=watermark)
    baseImage.save(outputImage)

    return baseImage

original = "teleme.jpg"
watermark = "meart.png"

create_watermark_image(original, "output.jpg", watermark, position=(0,0))
