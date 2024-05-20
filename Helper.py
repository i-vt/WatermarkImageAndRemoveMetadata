import os
def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def add_prepend(filepath: str, prepend: str):
    if prepend == "": return filepath
    if filepath != "":
        directory, file_name = os.path.split(filepath)
        if len(file_name) > (255 - len(prepend)): 
            file_name = file_name[len(prepend):]
        file_name = prepend + file_name
        filepath = os.path.join(directory, file_name)
    else: 
        print("Empty filepath supplied: add_prepend")
    return filepath

def get_image_file_size(image_path):
    try:
        return os.path.getsize(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return None