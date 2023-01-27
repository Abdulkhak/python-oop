import os

def list(path):
    if not os.path.exists(path):
        raise ValueError("FS operation failed: directory does not exist")
    for filename in os.listdir(path):
        print(filename)

def main():
    list("files")

if __name__ == "__main__":
    main()