import datetime
import time

class Timer:
    def __init__(self, second):
        self.__stopped = True
        self.__start_time = None
        self.__initial_second = second
        self.__second = second

    def __calculate(self):
        self.__second = self.__second - int(time.time() - self.__start_time)
        if self.__second <= 0:
            self.__stopped = True
            self.__second = 0
            self.__start_time = None


    def is_running(self):
        return not self.__stopped

    def get_time(self):
        if self.__start_time != None:
            self.__calculate()  
        return self.__second


    def start(self):
        self.__stopped = False
        self.__start_time = time.time()
        self.__second = self.__initial_second

    def stop(self):
        self.__second = 0
        self.__stopped = True
        self.__start_time = None
    
    def pause(self):
        self.__start_time = None
        self.__stopped = True

    def resume(self):
        self.__stopped = False
        self.__start_time = time.time()
