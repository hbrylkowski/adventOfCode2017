import unittest
import utils


class TestCaptcha(unittest.TestCase):
    test_examples_first = (
        ('1122', 3),
        ('1111', 4),
        ('1234', 0),
        ('91212129', 9),

    )

    def test_example(self):
        for t in self.test_examples_first:
            with self.subTest(captcha=t[0], result=t[1]):
                self.assertEqual(utils.reverse_captcha(t[0]), t[1])
