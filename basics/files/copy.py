import os
import shutil

def copy(src, dest):
    if not os.path.exists(src):
        raise ValueError("FS operation failed: files does not exist")
    if os.path.exists(dest):
        raise ValueError("FS operation failed: files_copy already exists")
    shutil.copytree(src, dest)

def main():
    copy("files", "files_copy")    

if __name__ == "__main__":
    main()
