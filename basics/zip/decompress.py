import zlib

def decompress(archive, filetodecompress):
    with open(archive, "rb") as fin, open(filetodecompress, "wb") as fout:
        decompressor = zlib.decompressobj()
        for chunk in iter(lambda: fin.read(1024 * 1024), b''):
            fout.write(decompressor.decompress(chunk))
        fout.write(decompressor.flush())

def main():
    decompress("archive.gz", "fileToCompress.txt")

if __name__ == "__main__":
    main()
    