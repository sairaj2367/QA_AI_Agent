import os

REFERENCE_DIR = 'reference_files'

def get_reference_content(file_name):
    file_path = os.path.join(REFERENCE_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return ""

def get_all_references():
    all_content = ""
    for file_name in os.listdir(REFERENCE_DIR):
        all_content += get_reference_content(file_name) + "\n\n"
    return all_content