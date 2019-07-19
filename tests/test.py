import unittest
import sys 
sys.path.append('../bustracker')

if sys.version_info < (2, 7):
    from unittest2 import main as test_main, SkipTest, TestCase
else:
    from unittest import main as test_main, SkipTest, TestCase

from bustracker import BusTracker

class TestStock(TestCase):

    def setUp(self):
        self.ttc = BusTracker('ttc')

    def test_predictions(self):
        stops = [
            {'routeTag': 506, 'stopTag': 3292},
            {'routeTag': 83, 'stopTag': 7871}
        ]

        predictions = self.ttc.get_predictions(stops)        
        self.assertTrue(isinstance(predictions, dict))

if __name__ == '__main__':
    test_main.main()