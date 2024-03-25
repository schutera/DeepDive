import unittest

from deep_dive.src import adder

class TestAdder(unittest.TestCase):

    def test_add_positive_integers(self):
        self.assertEqual(adder.add(5, 6), 11)

if __name__ == '__main__':
    unittest.main()