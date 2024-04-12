#ex1
import os

def list_directories_files(path):
    try:
        # Remove double quotes if present
        path = path.strip('"')

        # Get a list of all items (directories and files) in the specified path
        all_items = os.listdir(path)

        # Separate directories and files
        directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

        print(f"Directories in {path}:")
        for dir_name in directories:
            print(f"  {dir_name}")

        print(f"\nFiles in {path}:")
        for file_name in files:
            print(f"  {file_name}")

    except FileNotFoundError:
        print(f"Path '{path}' does not exist.")

# Example usage
user_path = input("Enter a path: ")
list_directories_files(user_path)




#ex2
import os

def check_path_access(path):
    try:
        # Check existence
        if os.path.exists(path):
            print(f"Path '{path}' exists.")
        else:
            print(f"Path '{path}' does not exist.")
            return

        # Check readability
        if os.access(path, os.R_OK):
            print(f"Path '{path}' is readable.")
        else:
            print(f"Path '{path}' is not readable.")

        # Check writability
        if os.access(path, os.W_OK):
            print(f"Path '{path}' is writable.")
        else:
            print(f"Path '{path}' is not writable.")

        # Check executability
        if os.access(path, os.X_OK):
            print(f"Path '{path}' is executable.")
        else:
            print(f"Path '{path}' is not executable.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_path = input("Enter a path: ")
check_path_access(user_path)


#ex3
import os

def analyze_path(path):
    try:
        # Check if the path exists
        if os.path.exists(path):
            print(f"Path '{path}' exists.")
            # Get the filename and directory portion
            filename = os.path.basename(path)
            directory = os.path.dirname(path)
            print(f"Filename: {filename}")
            print(f"Directory: {directory}")
        else:
            print(f"Path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_path = input("Enter a path: ")
analyze_path(user_path)



#ex4
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0

# Example usage
user_file_path = input("Enter the path to the text file: ")
line_count = count_lines_in_file(user_file_path)
print(f"Number of lines in '{user_file_path}': {line_count}")


#ex5
def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
user_file_path = input("Enter the path to the output file: ")
my_list = [1, 2, 3, 4, 5]
write_list_to_file(user_file_path, my_list)




#ex6
import string

def generate_alphabet_files():
    alphabet = string.ascii_uppercase

    for letter in alphabet:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}\n")
        print(f"File '{file_name}' created successfully.")

# Generate the alphabet files
generate_alphabet_files()


#ex7
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'w') as dest:
                dest.write(content)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")

# Example usage
source_path = input("Enter the path to the source file: ")
destination_path = input("Enter the path to the destination file: ")
copy_file(source_path, destination_path)





#ex8
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'w') as dest:
                dest.write(content)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")

# Example usage
source_path = input("Enter the path to the source file: ")
destination_path = input("Enter the path to the destination file: ")
copy_file(source_path, destination_path)