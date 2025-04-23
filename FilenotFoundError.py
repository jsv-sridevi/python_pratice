#here we are using class FilenotFoundError it tells whether file is in present directory or not
import os #here iswe imported because to check whether the file present in directory or not
try:
    file_path=input("enter the file name: ")
    if os.path.exists(file_path):
        with open(file_path,mode='rb') as file:
            read_data =file.read()
            print(read_data)
    else:
        print(f"Error: File '{file_path}' not found in the current directory.")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")


