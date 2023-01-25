from timer import Timer
import time

def main():
    t = Timer(3)
    t.start() # starting timer
    print(t.get_time()) # 100 seconds
    time.sleep(10)
    print(t.get_time()) # 97 seconds
    print(t.is_running())
if __name__ == "__main__":
    main()