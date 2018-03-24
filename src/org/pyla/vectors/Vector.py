# This package defines the concept of vectors and operations performed on the same.

class Vector(object):
    """
    This defines the concept of a mathematical vector of n dimensions
    A mathematical vector is represented as a pandas sequence indexed
    from 0 to n internally
    """
    def __init__(this, series):
        this.__series = series

    def __len__(self):
        return self.__series.size

    def __getitem__(self, item):
        return self.__series[item]
