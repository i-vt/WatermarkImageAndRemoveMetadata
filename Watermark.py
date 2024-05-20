from PIL import Image, ImageDraw, ImageFont
import os
import random
from Helper import *

def add_watermark(input_image_path, watermark_text, 
                    output_image_path, position=None, 
                    opacity=25, font_size=15, 
                    font_path=None,  color=(255, 0, 0)) -> bool:
    try:
        base_image = Image.open(input_image_path).convert("RGBA")
        txt = Image.new('RGBA', base_image.size, (255, 255, 255, 0))

        if font_path:
            fnt = ImageFont.truetype(font_path, font_size)
        else:
            fnt = ImageFont.load_default()

        d = ImageDraw.Draw(txt)

        # Get text size directly using getbbox
        left, top, right, bottom = d.textbbox((0, 0), watermark_text, font=fnt)
        text_width = right - left
        text_height = bottom - top
        
        if position is None:
            position = (base_image.width - text_width - 10, base_image.height - text_height - 10)

        d.text(position, watermark_text, font=fnt, fill=(*color, opacity))  # Unpack color tuple
        watermarked = Image.alpha_composite(base_image, txt)

        #watermarked.show()

        if output_image_path.lower().endswith('.png'):
            watermarked.save(output_image_path)
        else:
            watermarked = watermarked.convert("RGB")
            watermarked.save(output_image_path)
        return True
    except FileNotFoundError:
        print(f"Error: Image file not found at '{input_image_path}'")
    except OSError as e:
        print(f"Error processing image: {e}")
    except Exception as e:
        print("Generic Error: ", e)
    
    return False


def get_image_dimensions(image_path):
    """Gets the width and height of an image in pixels."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return None, None




def add_random_watermark(input_image_path: str, watermark_text: str, 
                        output_image_path: str = "", 
                        prepend: str = "", font_size=15,
                        font_path=None, color=(254, 1, 1)) -> bool:
    x, y = get_image_dimensions(input_image_path)
    x1, y1 = random.randint(0, x), random.randint(0, y)
    position = (x1,y1)
    
    opacity = random.randint(50, 255)
    
    if color == (254, 1, 1):
        color=(random.randint(0,256),random.randint(0,256),random.randint(0,256))
    

    if prepend == "": prepend = "watermarked_"

    if output_image_path == "": 
        output_image_path = add_prepend(input_image_path, prepend)

    # print(input_image_path, watermark_text, output_image_path, position, opacity, font_size, font_path, color)
    result = add_watermark(input_image_path, watermark_text ,output_image_path, 
                            position=position, opacity=opacity, 
                            font_size=font_size, font_path=font_path, color=color)
    return result


def add_many_watermarks(input_image_path: str, watermark_text: str, quantity: int=10, 
                        output_image_path: str = "") -> bool:
    prepend = "fullywatermarked_"
    #if prepend in input_image_path: continue
    watermark_text_big = ((watermark_text + '   ')*50 + "\n")*100
    if output_image_path == "": 
        output_image_path = add_prepend(input_image_path, prepend)

    if add_watermark(input_image_path, watermark_text_big, output_image_path) == False: 
        print("Failed to add watermark_text_big")
        return False
    for i in range(quantity): 
        if add_random_watermark(output_image_path, watermark_text, output_image_path) == False:
            print("Failed to add watermark_text")
            return False
    return True


def watermark_directory(directory, watermark_text, skip_already_watermarked: bool = False, image_extensions: list = ["jpg", "jpeg", "png"]):
    images_original = []
    images_watermarked = []
    
    for file in get_all_files(directory):
        extension = file.split(".")[-1]
        if extension in image_extensions:
            prepend_keyword = "watermarked_"
            if skip_already_watermarked and (prepend_keyword in file): continue
            images_original.append(file)
            image_watermarked_name = os.path.join(os.path.dirname(file), prepend_keyword + os.path.basename(file))
            images_watermarked.append(image_watermarked_name)
            try:
                print(file, "-?->", image_watermarked_name)
                add_many_watermarks(file, watermark_text, 10, image_watermarked_name)
            except Exception as ex:
                print(ex)
                if images_watermarked != 0 and images_original != 0:
                    images_watermarked[-1] = "FAILED TO OUTPUT"
                    print(f"FAILED TO OUTPUT: [{images_original[-1]}]")
            
        else: continue
    return images_original, images_watermarked
    
