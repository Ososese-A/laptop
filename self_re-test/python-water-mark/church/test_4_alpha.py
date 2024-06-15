from PIL import Image

def mark_image(inputImage, outputImage, marker):
    baseImage = Image.open(inputImage)
    watermark = Image.open(marker)
    base_width, base_height = baseImage.size
    mark_width, mark_height = watermark.size
    marker_offset_x = 96
    marker_offset_y = 64
    # mark_pos_x = base_width - (marker_offset_x + mark_width)
    mark_pos_x = marker_offset_x
    mark_pos_y = base_height - (marker_offset_y + mark_height)
    # print(base_height, base_width, mark_height, mark_width)

    baseImage.paste(watermark, (mark_pos_x, mark_pos_y), mask=watermark)
    baseImage.save(outputImage)

    return baseImage

original = "copy.png"
watermark = "super.png"

mark_image(original, "output_2.jpg", watermark)
