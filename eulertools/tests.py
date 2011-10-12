# vim: sw=4:ts=4:et:ai
import unittest
import doctest

import eulertools
import eulertools.factorization
import eulertools.modular
import eulertools.prime
import eulertools.probability

def load_tests(loader, tests, ignore):
    """ Add doctest test cases to unittest """
    tests.addTests(doctest.DocTestSuite(eulertools))
    tests.addTests(doctest.DocTestSuite(eulertools.factorization))
    tests.addTests(doctest.DocTestSuite(eulertools.modular))
    tests.addTests(doctest.DocTestSuite(eulertools.prime))
    tests.addTests(doctest.DocTestSuite(eulertools.probability))
    return tests

if __name__ == '__main__':
    unittest.main()

