import os

def parse_env_vars():
    d = {}
    for key, value in os.environ.items():
        if key.startswith("RSS_"):
            d[key] = value

    ans = []
    for key, value in d.items():
        ans.append(f"{key}={value}")

    print("; ".join(ans))

def main():
    parse_env_vars()

if __name__ == "__main__":
    main()