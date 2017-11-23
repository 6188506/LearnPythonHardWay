def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function(7, 8)
    82
    """

    return a * b
	
if __name__=='__main__':
    import doctest
    doctest.testmod()	