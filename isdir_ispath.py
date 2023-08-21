import os

def directory_exists(path):
    return os.path.exists(path) and os.path.isdir(path)

def main():
    directory_path = input("Enter the directory path: ")
    
    if directory_exists(directory_path):
        print(f"The directory '{directory_path}' exists.")
    else:
        print(f"The directory '{directory_path}' does not exist.")

if __name__ == "__main__":
    main()
