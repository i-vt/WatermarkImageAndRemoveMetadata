import os
import argparse
from Watermark import *
from RemoveImageMetadata import *

def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def add_prepend(filepath: str, prepend: str):
    if prepend == "":
        return filepath
    if filepath != "":
        directory, file_name = os.path.split(filepath)
        if len(file_name) > (255 - len(prepend)):
            file_name = file_name[len(prepend):]
        file_name = prepend + file_name
        filepath = os.path.join(directory, file_name)
    else:
        print("Empty filepath supplied: add_prepend")
    return filepath

def clean_directory(directory, skip_already_cleaned: bool = False, image_extensions: list = ["jpg", "jpeg", "png"]):
    images_original = []
    images_cleaned = []

    for file in get_all_files(directory):
        extension = file.split(".")[-1]
        if extension in image_extensions:
            if skip_already_cleaned and ("cleaned_" in file):
                continue
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

        else:
            continue
    return images_original, images_cleaned

def watermark_directory(directory, watermark_text, skip_already_watermarked: bool = False, image_extensions: list = ["jpg", "jpeg", "png"]):
    images_original = []
    images_watermarked = []

    for file in get_all_files(directory):
        extension = file.split(".")[-1]
        if extension in image_extensions:
            prepend_keyword = "watermarked_"
            if skip_already_watermarked and (prepend_keyword in file):
                continue
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

        else:
            continue
    return images_original, images_watermarked

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Watermark images and remove metadata from a directory.')
    parser.add_argument('--dir', type=str, required=True, help='Directory containing images')
    parser.add_argument('--watermark', type=str, required=True, help='Watermark text to apply to images')
    parser.add_argument('--skip-cleaned', action='store_true', help='Skip images that are already cleaned')
    parser.add_argument('--skip-watermarked', action='store_true', help='Skip images that are already watermarked')
    parser.add_argument('--clean', action='store_true', help='Remove metadata from images')
    parser.add_argument('--watermarking', action='store_true', help='Apply watermark to images')

    args = parser.parse_args()

    if args.clean:
        original, cleaned = clean_directory(args.dir, args.skip_cleaned)
        print("\nCleaning:")
        for i in range(len(original)):
            print(original[i], "->", cleaned[i])

    if args.watermarking:
        original, watermarked = watermark_directory(args.dir, args.watermark, args.skip_watermarked)
        print("\nWatermarking:")
        for i in range(len(original)):
            print(original[i], "->", watermarked[i])
