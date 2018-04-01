import math
import unittest

import numpy as np

from org.pyla.vectors import vector

class VectorTest(unittest.TestCase):
    """
    This class defines the unit tests for Vector class
    """

    def test_length(self):
        """
        Unit test for length function in vector class.
        """
        test_vector = vector.Vector(np.arange(5))
        self.assertEqual(test_vector.length(), math.sqrt(30))

    def test_dot_product(self):
        """
        Unit test for dot_product function in vector class.
        """
        test_vector1 = vector.Vector(np.arange(5))
        test_vector2 = vector.Vector(np.arange(5))

        self.assertEqual(test_vector1.dot_product(test_vector2), 30)


if __name__ == '__main__':
    unittest.main()