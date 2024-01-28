from django.test import SimpleTestCase
from app import calc

"""test the cal module"""


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """test adding two numbers"""
        res = calc.add(3, 4)
        self.assertEqual(res, 7)
