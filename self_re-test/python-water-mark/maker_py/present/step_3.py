from PIL import Image

def mark_image(inputImage, outputImage, marker):
    baseImage = Image.open(inputImage)
    watermark = Image.open(marker)
    base_width, base_height = baseImage.size
    mark_width, mark_height = watermark.size
    marker_offset_x = 80
    marker_offset_y = 40
    mark_pos_x = base_width - (marker_offset_x + mark_width)
    mark_pos_x = marker_offset_x
    mark_pos_y = base_height - (marker_offset_y + mark_height)
    # mark_pos_y = marker_offset_y

    baseImage.paste(watermark, (mark_pos_x, mark_pos_y), mask=watermark)
    baseImage.save(outputImage)

    return baseImage