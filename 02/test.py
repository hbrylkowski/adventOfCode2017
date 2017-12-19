import unittest
import utils


class TestCaptcha(unittest.TestCase):
    def test_example(self):
        spreadsheet = """5 1 9 5
7 5 3
2 4 6 8"""
        self.assertEqual(utils.checksum(spreadsheet, " "), 18)


    def test_example_modulo(self):
        spreadsheet = """5 9 2 8
9 4 7 3
3 8 6 5"""
        self.assertEqual(utils.checksum_modulo(spreadsheet, " "), 9)
