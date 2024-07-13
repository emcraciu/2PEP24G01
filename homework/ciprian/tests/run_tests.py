import unittest

from homework.ciprian.tests.mytest import data_getter


OUTPUT = [{'FSLY': 7.44, 'LI': 21.28, 'PLUG': 3.07, 'SPWR': 2.69, 'XPEV': 8.84},
          {'FSLY': -0.53, 'LI': -0.75, 'PLUG': 4.78, 'SPWR': 5.91, 'XPEV': 1.73}]

class TestYahooDataRetrival(unittest.TestCase):
    def test_connection(self):
        self.assertEqual(
            data_getter(),
            OUTPUT
        )



