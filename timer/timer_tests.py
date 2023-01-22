import unittest
from timer import Timer 
import time

class TestTimer(unittest.TestCase):

    def test_timer_constructor(self):
        t = Timer(10)
        self.assertEqual(t.get_time(), 10, "Should be 10")
        t.start()
        time.sleep(3)      
        self.assertEqual(t.get_time(), 7, "Should be 7")
        t.stop()
        self.assertEqual(t.get_time(), 0, "Should be 0")
        self.assertEqual(t.is_running(), False, "Should be False")
        t.start()
        self.assertEqual(t.get_time(), 10, "Should be 10")
        time.sleep(4)
        self.assertEqual(t.get_time(), 6, "Should be 6")
        t.pause()
        self.assertEqual(t.get_time(), 6, "Should be 6")
        time.sleep(3)
        self.assertEqual(t.get_time(), 6, "Should be 6")
        t.resume()
        time.sleep(4)
        self.assertEqual(t.get_time(), 2, "Should be 2")  
                
if __name__ == '__main__':
    unittest.main()