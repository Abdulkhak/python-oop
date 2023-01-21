from timer import Timer
import time

def main():
    t = Timer(100)
    t.start() # starting timer
    print(t.get_time()) # 100 seconds
    time.sleep(3)
    print(t.get_time()) # 97 seconds
    t.stop()
    print(t.get_time()) # 0 seconds
    t.start() # 100
    time.sleep(10)
    print(t.get_time()) #90
    t.pause()
    print(t.get_time()) #90
    time.sleep(3)
    print(t.get_time()) # 90 seconds
    t.resume()
    time.sleep(5)
    print(t.get_time()) # 85 seconds

if __name__ == "__main__":
    main()