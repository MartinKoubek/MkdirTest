'''
This is pyhon "main" script

It checks Linux OS and runs all tests in this folder(s)
No parameter required.

Created on Jun 17, 2021

@author: Martin Koubek
'''

import unittest
import sys

if __name__ == "__main__":
    if not sys.platform.startswith('linux'):
        print ("Tests must run on Linux OS")
        sys.exit(0)
        
    '''
    Load all tests in a folder
    '''
    loader = unittest.TestLoader()
    tests = loader.discover('.', pattern="*.py")
    testRunner = unittest.runner.TextTestRunner(stream=sys.stdout, 
                                                verbosity=2)

    """
    Process results
    """
    result = testRunner.run(tests)
    if len(result.errors) == 0 and len(result.failures) == 0 :
        print ("/**TEST PASSED: all ", result.testsRun, "tests passed**/")
        sys.exit(0)
    else:
        print ("/**TEST FAILED: ", 
               len(result.errors) + len(result.failures), " from ", 
               result.testsRun, " tests failed or was erronerous**/")
        sys.exit(1)
