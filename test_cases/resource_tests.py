"""
Resource utilization tests are test process aimed to determine the resource 
usage of a software product.

Testing was devided to:
* CPU
* MEM

Created on Jun 17, 2021
@author: Martin Koubek
"""

import os
import time
import subprocess

from test_cases.base_test import BaseTest
from helper.mkdir import MkDir


class ResourceTest(BaseTest):

    def test_in_timelimit(self):
        """
        Test if directory is created in time
        Expectation: directory created in 0.01 sec
        """
        start_time = time.time()
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        MkDir().run([directory])

        self.assertLessEqual(time.time() - start_time, 0.01,
                             "Directory creation takes too much time")

    def test_cpu_usage(self):
        """
        Test if directory is created without overloading CPU
        Expectation: directory created and CPU do not change more then 1%
        """
        start_cpu = self.__get_cpu()
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        MkDir().run([directory])

        self.assertLessEqual(abs(self.__get_cpu() - start_cpu), 1,
                             "Directory creation takes too much CPU")

    def test_mem_usage(self):
        """
        Test if directory is created without eating memory
        Expectation: directory created and memory does not rise more then 10kB
        """
        start_mem = self.__get_mem()
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        MkDir().run([directory])

        self.assertLessEqual(abs(self.__get_mem() - start_mem), 10,
                             "Directory creation takes too much MEM")

    def __get_cpu(self):
        """
        Helper function to get CPU
        """
        return float(self.__call_command(
            r"grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} "
            "END {print usage}'")
        )

    def __get_mem(self):
        """
        Helper function to get memory size
        """
        return int(self.__call_command(
            r"free -m | grep 'Mem' |awk '{print $3}'"))

    def __call_command(self, command):
        """
        Helper function to call a command
        Using SHEL=True used for more complex command. Definetly "shall"
        could be set to False to avoid  complexity and overhead.
        In this example, shell=True was used for simplicity
        """
        proc = subprocess.run(command,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
        return  proc.stdout.decode().strip()
