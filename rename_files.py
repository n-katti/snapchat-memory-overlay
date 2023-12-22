import os
import re
from pathlib import Path

# location = os.path.abspath(__file__)

# os.chdir(os.path.dirname(location))

# directory_path = r'C:\Users\nikhi\OneDrive\Documents\Python Projects\snapchat-memory-overlay\input\memories'

#Function to remove the matched date format from each file name
def remove_date_prefix(file_name, pattern):
    match = re.match(pattern, file_name)
    if match:
        return match.group(2)
    else:
        return file_name

def rename_without_date_prefix(memory_folder: Path):
    
    # Define a regular expression pattern to match the mm-dd-yyyy_ part at the beginning of each file name
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2}_)(.*)')

    # List all files in the specified directory
    files = os.listdir(memory_folder)


    # Filter only files (excluding directories)
    files = [file for file in files if os.path.isfile(os.path.join(memory_folder, file))]

    for file in files:
        old_path = os.path.join(memory_folder, file)
        new_name = remove_date_prefix(file, pattern)
        new_path = os.path.join(memory_folder, new_name)
        os.rename(old_path, new_path)