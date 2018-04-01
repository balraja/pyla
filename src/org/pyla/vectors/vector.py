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
        self.__length = math.sqrt(np.sum(np.multiply(self.__array, self.__array)))

    @property
    def numpy_array(self):
        """
        :return: Returns underlying numpy rray
        """
        return self.__array

    @property
    def length(self):
        """
        Returns length of a vector. The length of a vector is obtained as
        a sqrt of dot product with itself.

        :return: mathematical length of a vector.
        """
        return self.__length

    def __validate_other_operand(self, other_vector):
        """
        A private method to check other vector that's a parameter
        of binary operations on vectors
        """
        if not isinstance(other_vector, Vector):
            raise "The other_vector is not of the Vector type"

        if (self.__array.shape != other_vector.__array.shape):
            raise "The shape of arrays in vectors don't match"

        if (self.__array.dtype != other_vector.__array.dtype):
            raise "The type of arrays in vectors don't match"


    def add(self, other_vector):
        """
        Defines mathematical vector addition, wherein sum of a vector is
        calculated as sum of its components.

        :param other_vector: The vector to be summed up with this vector.
        :return: A vector that's sum of the components of two vectors
        """
        self.__validate_other_operand(other_vector)
        return Vector(np.add(self.__array, other_vector.__array))

    def scalar_multiplication(self, scalar):
        """
        Defines scalar multiplication of a vector wherein a given scalar
        is multiplied with the components of a vector.

        :param scalar: The scalar with which the multiplication happens.
        :return: A vector whose components are multiplied with scalar
        """
        return Vector(self.__array * scalar)

    def unit_vector(self):
        """
        :return: Returns an unit length vector of itself, i.e. vector / length
        """
        return Vector(self.__array / self.__length)

    def dot_product(self, other_vector):
        """
        Defines mathematical dot products between vectors

        :param other_vector: The other vector that's participating in the dot product
        :return: A scalar representing the dot product between vectors
        """
        self.__validate_other_operand(other_vector)

        return np.sum(np.multiply(self.__array, other_vector.__array))

    def scalar_projection(self, projected_vector):
        """
        This method returns the scalar length of projection of provided vector
        into this vector

        :param projected_vector: The vector that's projected on to this vector
        :return: the scalar length of projection
        """

        dot_product = self.dot_product(projected_vector)
        return dot_product / self.__length

    def vector_projection(self, projected_vector):
        """
        This method returns the projection of another vector onto this vector as a
        vector in the same direction as this vector

        :param projected_vector: The vector that's projected on to this vector
        :return: The vector that defines the projection
        """
        scalar_projection = self.scalar_projection(projected_vector)
        return self.unit_vector().scalar_multiplication(scalar_projection)

    def __repr__(self):
        return repr(self.__array)

    def __str__(self):
        return str(self.__array)