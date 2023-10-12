import os
import argparse

def is_file_or_directory(path):
    if os.path.isfile(path):
        return "File"
    elif os.path.isdir(path):
        return "Directory"
    else:
        return "Other"

def list_files_in_directory(directory):
    for root, dirs, files in os.walk(directory, followlinks=True):
        for name in files + dirs:
            path = os.path.join(root, name)
            file_type = is_file_or_directory(path)
            print(f"{path} is a {file_type}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively list files and directories in a specified directory.")
    parser.add_argument("directory_path", help="The starting directory path")
    args = parser.parse_args()

    if os.path.exists(args.directory_path) and os.path.isdir(args.directory_path):
        list_files_in_directory(args.directory_path)
    else:
        print("Invalid directory path. Please provide a valid directory path.")

