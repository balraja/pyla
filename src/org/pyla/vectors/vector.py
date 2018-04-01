import math

import numpy as np

class Vector(object):
    """
    This defines the concept of a mathematical vector of n dimensions
    A mathematical vector is represented as a numpy array indexed
    from 0 to n-1 internally
    """
    def __init__(self, np_array):
        """
        CTOR

        :param np_array: The data of a vector as one dimensional array
        """
        if (np_array.ndim != 1):
            raise "The underlying arrays of vectors should be a single dimensional"
        self.__array = np_array

    def length(self):
        """
        Returns length of a vector. The length of a vector is obtained as
        a sqrt of dot product with itself.

        :return: mathematical length of a vector.
        """
        return math.sqrt(np.sum(np.multiply(self.__array, self.__array)))

    def dot_product(self, other_vector):
        """
        Defines mathematical dot products between vectors

        :param other_vector: The other vector that's participating in the dot product
        :return: A scalar representing the dot product between vectors
        """
        if not isinstance(other_vector, Vector):
            raise "The other_vector is not of the Vector type"

        if (self.__array.shape != other_vector.__array.shape):
            raise "The shape of arrays in vectors don't match"

        if (self.__array.dtype != other_vector.__array.dtype):
            raise "The type of arrays in vectors don't match"

        return np.sum(np.multiply(self.__array, other_vector.__array))


