import unittest

import tensorflow as tf

from deep_dive.src.__main__ import normalize

class TestAll(unittest.TestCase):

    def test_normalization(self):
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
        x_norm = normalize(x_train)
        expected_max_value = 10 # fixme
        assert x_norm.all() == (x_train/expected_max_value).all(), "A normalization is done by dividing each value by the max possible value. Which in our case is?"

if __name__ == '__main__':
    unittest.main()