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
        self.assertEqual(test_vector.length, math.sqrt(30))

    def test_dot_product(self):
        """
        Unit test for dot_product function in vector class.
        """
        test_vector1 = vector.Vector(np.arange(5))
        test_vector2 = vector.Vector(np.arange(5))

        self.assertEqual(test_vector1.dot_product(test_vector2), 30)

    def test_projection(self):
        """
        Unit test that defines the projections
        """
        test_vector = vector.Vector(np.arange(5))
        projected_vector = vector.Vector(np.ones(5, dtype=np.int64))
        self.assertEqual(test_vector.scalar_projection(projected_vector), 10 / math.sqrt(30))

        projection_as_vector = test_vector.vector_projection(projected_vector)
        self.assertTrue(np.all(projection_as_vector.numpy_array == 10/30 * np.arange(5)))


if __name__ == '__main__':
    unittest.main()