import unittest
import Part1
class TestPart1(unittest.TestCase):

# we need to write a method for the test
    def test_add(self):
        result = Part1.add(10,5)
        self.assertEqual(result, 15)