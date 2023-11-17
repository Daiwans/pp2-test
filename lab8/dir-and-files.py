#1
import os

def list_dirs_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

path = '/your/specified/path'
dirs, files = list_dirs_files(path)
print("Directories:", dirs)
print("Files:", files)

#2
def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

path = '/your/specified/path'
access_info = check_access(path)
print("Exists, Readable, Writable, Executable:", access_info)

#3
def path_details(path):
    exists = os.path.exists(path)
    if exists:
        directory, filename = os.path.split(path)
        return directory, filename
    return None, None

path = '/your/specified/path'
directory, filename = path_details(path)
if directory and filename:
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist.")

#4
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

filename = 'yourfile.txt'
line_count = count_lines(filename)
print("Number of lines:", line_count)

#5
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

data = ['line1', 'line2', 'line3']
write_list_to_file(data, 'output.txt')

#6
def generate_alphabet_files():
    for char in range(65, 91):  # ASCII values for A to Z
        with open(f"{chr(char)}.txt", 'w') as file:
            file.write(f"This is {chr(char)}.txt")

generate_alphabet_files()

#7
def copy_file(src, dest):
    with open(src, 'r') as source, open(dest, 'w') as destination:
        destination.write(source.read())

copy_file('source.txt', 'destination.txt')

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or is not writable.")

file_path = '/path/to/your/file.txt'
delete_file(file_path)
