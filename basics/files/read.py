import os

def read(file):
    if not os.path.exists(file):
        raise ValueError("FS operation failed: file does not exist")
    with open(file) as f:
        print(f.read())

def main():
    read("fileToRead.txt")

if __name__ == "__main__":
    main()