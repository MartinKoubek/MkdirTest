"""
Fault testing is a testing technique which sets system conditions a way, 
the software system fails:

Testing was devided to:
* no permission 
* no disk space
* foder already exists

Created on Jun 17, 2021

@author: Martin Koubek
"""

import os
import subprocess

from test_cases.base_test import BaseTest
from helper.mkdir import MkDir


class FaultTest(BaseTest):
    def test_no_permission(self):
        """
        Test directory creation in directory without permision for writting 
        Expectation: directory is not created
        """
        os.system('chmod ugo-rwx ' + self.DEFAULT_FOLDER_PATH)
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")

        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(1, exit_code,
                         "Exit code did NOT raise for folder creation:" +
                         stderr)
        self.assertFalse(os.path.exists(directory),
                         "Directory was not created:" + stderr)

    def test_folder_exists(self):
        """
        Test directory creation if directory already exists 
        Expectation: directory is not created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        os.mkdir(directory)

        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(1, exit_code,
                         "Exit code did NOT raise for folder creation:" +
                         stderr)

    def test_disk_is_full(self):
        """
        Test directory creation if disk space is full
        Expectation: directory is not created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        command = MkDir().COMMAND + " " + directory + " " + \
            MkDir.ArgumentsName.VERBOSE + " >/dev/full"

        proc = subprocess.run(command,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)

        exit_code = proc.returncode
        self.assertGreater(
            exit_code,
            0,
             "Exit code did NOT raise for folder creation"
             )
