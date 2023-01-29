import hashlib

def calc_hash():
    
    with open("fileToCalculateHashFor.txt", "rb") as f:
        rb_data = f.read()
    
    sha256 = hashlib.sha256()
    sha256.update(rb_data)
    to_hex = sha256.hexdigest()
    print(to_hex)

def main():
    calc_hash()

if __name__ == "__main__":
    main()