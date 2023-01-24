import datetime
import time

class Timer:
    def __init__(self, second):
        self.__start_time = None
        self.__initial_second = second
        self.__second = second
        self.expired = False
        self.paused = False
        self.running = False

    def start(self):
        self.running = True
        self.paused = False
        self.expired = False
        self.__start_time = time.time()
        self.__second = self.__initial_second
        self.__calculate()

    def get_time(self):
        return self.__second

    def is_running(self):
        return self.running and not self.expired

    def __calculate(self):
        self.__second = self.__second - int(time.time() - self.__start_time)
        if self.__second <= 0:
            self.__stop()

    def __stop(self):
        self.__second = 0
        self.running = False
        self.expired = True
        self.__start_time = None

    def stop(self):
        self.__stop()
    
    def pause(self):
        if self.running:
            self.paused = True
            self.running = False
            self.__second = self.__second - int(time.time() - self.__start_time)
            self.__start_time = None

    def resume(self):
        if self.paused:
            self.running = True
            self.paused = False
            self.__start_time = time.time()

