from timer import Timer 
import time
import mock
from mock import patch
from unittest import TestCase
from unittest.mock import patch
import unittest

class TestTimer(unittest.TestCase):
    
    def test_timer_constructor(self):
        t = Timer(10)
        self.assertEqual(t.get_time(), 10, "Should be 10")
        self.assertFalse(t.is_running(), "Should not be runnning")

    def test_timer_is_running_when_started(self):
        t = Timer(10)
        t.start()
        self.assertTrue(t.is_running(), "Should be running when start")

    def test_timer_is_not_running_when_paused(self):
        t = Timer(10)
        t.start()
        t.pause()
        self.assertFalse(t.is_running(), "Should not be running when pause")

    def test_timer_is_running_when_resumed(self):
        t = Timer(10)
        t.start()
        t.pause()
        t.resume()
        self.assertTrue(t.is_running(), "Should be running after resume")

    def test_timer_is_not_running_when_stopped(self):
        t = Timer(10)
        t.start()
        t.stop()
        self.assertFalse(t.is_running(), "Should not be running after stopped")

    def test_timer_seconds_after_stop(self):
        t = Timer(10)
        t.start()
        t.stop()
        self.assertEqual(t.get_time(), 0, "Should be 0 when timer stopped")

    @patch('time.time')
    def test_timer_stops_correctly(self, mock_time):
        mock_time.side_effect = [0, 11]
        t = Timer(10)
        t.start()
        self.assertEqual(t.get_time(), 0, "Should be 0 on finished timer")
    
    @patch('time.time')
    def test_timer_runs_correctly(self, mock_time):
        mock_time.side_effect = [0, 6]
        t = Timer(10)
        t.start()
        self.assertEqual(t.get_time(), 4, "Should be 4 after 6 seconds passes")
    
    @patch('time.time')
    def test_timer_gives_correct_remaining_time_when_paused(self, mock_time):
        mock_time.side_effect = [0, 6]
        t = Timer(10)
        t.start()
        t.pause()
        self.assertEqual(t.get_time(), 4, "Should be 4 after 6 seconds passes")
    
    @patch('time.time')
    def test_timer_is_not_running_when_time_expires(self, mock_time):
        mock_time.side_effect = [0, 20]
        t = Timer(10)
        t.start()
        self.assertEqual(t.get_time(), 0, "Timer should have expired after 20 seconds")
        self.assertFalse(t.is_running(), "Should not be running after time expires")
        
if __name__ == '__main__':
    unittest.main()
