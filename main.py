from Watermark import *
from RemoveImageMetadata import *

if __name__ == "__main__":
    processing_dir = "/Users/user/Projects/ImageLaundermat/" # changeme


    original, cleaned = clean_directory(processing_dir, True)
    print("\nCleaning:")
    for i in range(len(original)):
        print(original[i], "->", cleaned[i])
    original, watermarked = watermark_directory(processing_dir, "br 23 ap", True)
    print("\nCleaning:")
    for i in range(len(original)):
        print(original[i], "->", watermarked[i])