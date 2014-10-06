py-arc4random
=============

Basic python 2.7/3 implementation of OpenBSDs arc4random PRNG.

Example
-------

    $ python
    >>> import arc4random
    >>> arc4random.rand()
    2057591911
    >>> arc4random.randrange(50,100)
    75
    >>> arc4random.randsample(0,1, 10)
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
