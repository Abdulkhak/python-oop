import os

def create_file():
    file = 'fresh.txt'
    if os.path.isfile(file):
        raise Exception("FS operation failed: file already exists.")
    with open(file, 'w') as f:
        f.write("I am fresh and young")

def main():
    create_file()

if __name__ == '__main__':
    main()
