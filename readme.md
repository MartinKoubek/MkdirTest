# ASSIGNMENT


Design and create automated tests for mkdir linux(unix) command.

## Tasks:

1) Analyze functionality of mkdir command (study documentation if available)
2) Design test approach and create testcase(s)
3) Design automation approach and create automated test script(s)

### Expected outcome:

- Present functionality of tested product
- Present test approach selected for testing this product and testcases created for it
- Present portion of the automation you have created

### Automation requirements:

- [x] Write the automation in Python
     * see github project: https://github.com/MartinKoubek/MkdirTest

Automation output:
* [ ] When check passed print on stdout: "[PASS] <description of check>"
    * Need discussion with Test manager if stdout can follow unittest stndard format - format: <description of check>... [ok]
* [ ] When check failed print on stdout: "[FAIL] <description of check, explanation of failure>"
    * Need discussion with Test manager if stdout can follow unittest stndard format - format:  <description of check, explanation of failure> ... [FAIL]
* [X] If any check inside test script failed it should exit returning 1
        and print on stdout: "/**TEST FAILED: <number of failed checks, summary>**/"
* [X] If all check passed it should exit returning 0 and print on
        stdout: "/**TEST PASSED: <summary>**/"

### Notes:

- Full and complete automation is not needed to be done, but it is expected to develop several fully functional tests.
- You are expected to present your approach for testing and automation as well as some working code.
- You are expected to use your own laptop to demonstrate your solution via zoom shared screen.

## Description of work
* Unitests are writtent in python3.6 following recomendation from unittest framework: https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest
* As command "mkdir" is platform depeneded, the unittests are also platform dependend - running only on Linux OS
* Blackbox strategy of testing was choosen as mkdir command is a linux command that is undevidable to smaller parts 
* Only stdin input is used for setting command parameters and stdout and stderr is used for reading output of command. No other interface are tested.

### Testing strategy
There is presented several testing strategy.

#### Functional testing
FUNCTIONAL TESTING is a type of software testing that validates the software system against the functional requirements/specifications. The purpose of Functional tests is to test each function of the software application, by providing appropriate input, verifying the output against the Functional requirements. 

Testing was devided to:
* smoke tests: was performed - test simple feature
* sanity check: was performed mainly with parameter "mode". Not all variations were tested. Only interesting combinations (letters, numbers) were tested. 
* regresion tests: was not performed in this example. Tests performed only on mkdir command in version "mkdir (GNU coreutils) 8.25"
* usability testing: was performed partly in "Testing resources"

#### Interface testing
Interface Testing is defined as a software testing type which verifies whether input and output of software system is is done correctly.

Testing was devided to:
* Character encoding - special chars, UTF-8, UTF-16
* Extra long name directories
* Invalid parameters
 
#### Fault behaviour testing
Fault testing is a testing technique which sets system conditions a way, the software system fails:

Testing was devided to:
* no permission 
* no disk space
* foder already exists

#### Error injections testing
Error or Fault injection is a testing technique which aids in understanding how a [virtual/real] system behaves when stressed in unusual ways.

This testing was not done as mkdir command is very simple which makes this testing imposible.

For complex software system, the following strategies would be used:
* killing some of software system subprocess
* TCP/UDP communication
  * unrealible connections
  * unreable counterpart of system
* CPU/memory overloading
* Disk out of space
* Change of permissions

#### Resources testing
Resource utilization tests are test process aimed to determine the resource usage of a software product.

Testing was devided to:
* CPU
* MEM

### How to run

<code>
python3 mkdir_test.py
</code>

### Findings

Some functional tests fail. It need be discussed, whether it is failing function or this is intention from author of mkdir. These tests are marked as FAIL_test_* and they do not run by default
 
