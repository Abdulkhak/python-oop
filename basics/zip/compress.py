import zlib

def compress(filetocomress, archive):
    with open(filetocomress, "rb") as fin, open(archive, "wb") as fout:
        compressor = zlib.compressobj(level = 9)
        for chunk in iter(lambda: fin.read(1024 * 1024), b''):
            fout.write(compressor.compress(chunk))
        fout.write(compressor.flush()) 

def main():
    compress("fileToCompress.txt", "archive.gz")

if __name__ == "__main__":
    main()
    