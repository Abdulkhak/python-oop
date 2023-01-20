import datetime
import time

class Timer:
    def __init__(self, hour, minute, second):
        self.__second = second
        self.__minute = minute
        self.__hour = hour
        self._stopped = True
        self._totalseconds = self.__hour * 3600 + self.__minute * 60 + self.__second

    def get_minute(self):
        return self.__minute
  
    def get_hour(self):
        return self.__hour

    def get_second(self):
        return self.__second
 
    def get_formatted(self):
        return datetime.timedelta(seconds = self._totalseconds)     

    def start(self):
        while self._totalseconds > 0 and self._stopped != False:
            print(self.get_formatted(), end="\r")
            time.sleep(1)
            self._totalseconds -= 1
        print("Time us up!")

    def stop(self):
        self._totalseconds = 0
        self.start()
    
    def pause(self):
        self._stopped = False
        print(self.get_format(), end="\r")

    def resume(self):
        self._stopped = True
        self.start()
   

t = Timer(0,0,5)
t.start()
t.stop()