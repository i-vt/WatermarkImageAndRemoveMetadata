from PIL import Image
import os
from Helper import *

def remove_metadata(image_path, output_path):
  
    with Image.open(image_path) as img:
        if img.mode == 'RGBA': 
            img = img.convert('RGB')  # Convert to RGB to remove transparency

        data = img.getdata()
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(data)

        # Save the image without metadata
        new_img.save(output_path, "JPEG")  


def clean_directory(directory, skip_already_cleaned: bool = False, image_extensions: list = ["jpg", "jpeg", "png"]):
    images_original = []
    images_cleaned = []
    
    for file in get_all_files(directory):
        extension = file.split(".")[-1]
        if extension in image_extensions:
            if skip_already_cleaned and ("cleaned_" in file): continue
            images_original.append(file)
            image_cleaned_name = os.path.join(os.path.dirname(file), "cleaned_" + os.path.basename(file))
            images_cleaned.append(image_cleaned_name)
            try:
                remove_metadata(file, image_cleaned_name)
            except Exception as ex:
                print(ex)
                if images_cleaned != 0 and images_original != 0:
                    images_cleaned[-1] = "FAILED TO OUTPUT"
                    print(f"FAILED TO OUTPUT: [{images_original[-1]}]")
            
        else: continue
    return images_original, images_cleaned


