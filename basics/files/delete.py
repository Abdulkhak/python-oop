import os

def delete(src):
    if not os.path.exists(src):
        raise ValueError("FS operation failed: file does not exist")
    os.remove(src)

def main():
    delete("fileToRemove.txt")

if __name__ == "__main__":
    main()