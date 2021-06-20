"""
This is base class for unittests.

It helps to cleanup space. Unittest will have always cleanup starting point 
Created on Jun 17, 2021

@author: Martin Koubek
"""
import unittest
import os

class BaseTest(unittest.TestCase):
    DEFAULT_FOLDER_PATH = "/tmp/mkdir_test"
    
    def setUp(self):
        """
        Remove directory - in case of unittest crash and some mess remain
        Create fresh directory
        """
        self.__cleanup()
        os.mkdir(self.DEFAULT_FOLDER_PATH)


    def tearDown(self):
        """
        Remove directory when test finish
        """
        self.__cleanup()

    def __cleanup(self):
        """
        Used rm -rf command to ensure, the folder is always removed
        """
        os.system("rm -rf " + self.DEFAULT_FOLDER_PATH)