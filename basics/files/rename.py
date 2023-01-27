import os

def rename(src, dest):
    if not os.path.exists(src):
        raise ValueError("FS operation failed: source file does not exist")
    if os.path.exists(dest):
        raise FileExistsError("FS operation failed: destination file already exists")
    os.rename(src, dest)

rename("wrongFilename.txt", "properFilename.md")
