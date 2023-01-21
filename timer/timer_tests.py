import unittest
from timer import Timer 

class TestTimer(unittest.TestCase):

    def test_timer_constructor(self):
        t = Timer(10)
        self.assertEqual(t.get_time(), 10, "Should be 10")
                

   
if __name__ == '__main__':
    unittest.main()