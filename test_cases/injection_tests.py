"""
Testing of error injections

Error or Fault injection is a testing technique which aids in understanding how a [virtual/real] system behaves when stressed in unusual ways.

This testing was not done as mkdir command is very simple which makes this testing imposible.

For complex software system, the following strategies would be used:

killing some of software system subprocess
TCP/UDP communication
unrealible connections
unreable counterpart of system
CPU/memory overloading
Disk out of space
Change of permissions

Created on Jun 17, 2021
@author: Martin Koubek
"""

from test_cases.base_test import BaseTest


class InjectionTest(BaseTest):
    """
    Injection Tests are not implemented
    https://en.wikipedia.org/wiki/Fault_injection'''
    """
    pass
