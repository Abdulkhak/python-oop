import sys

def parse_args():
    
    args = sys.argv[1:]
    d = {}

    for i, arg in enumerate(args):
        if arg.startswith("--"):
            d[arg[2:]] = args[i + 1]
    
    ans = []
    for key, value in d.items():
        ans.append(f"{key} is {value}")
    print(", ".join(ans))

def main():
    parse_args()

if __name__ == "__main__":
    main()