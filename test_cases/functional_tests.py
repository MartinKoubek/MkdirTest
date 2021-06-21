"""
FUNCTIONAL TESTING is a type of software testing that validates the software 
system against the functional requirements/specifications. 
The purpose of Functional tests is to test each function of the 
software application, by providing appropriate input, 
verifying the output against the Functional requirements. 

Testing was devided to:
* smoke tests: was performed - test simple feature
* sanity check: was performed mainly with parameter "mode". Not all variations 
were tested. Only interesting combinations (letters, numbers) were tested. 
* regresion tests: was not performed in this example. Tests performed only on 
mkdir command in version "mkdir (GNU coreutils) 8.25"
* usability testing: was performed partly in "Testing resources"

Created on Jun 17, 2021
@author: Martin Koubek
"""
import os

from test_cases.base_test import BaseTest
from helper.mkdir import MkDir


class FunctionalTest(BaseTest):
    """
    Description of mkdir command

    NAME         top

       mkdir - make directories

    SYNOPSIS         top

           mkdir [OPTION]... DIRECTORY...

    DESCRIPTION         top

       Create the DIRECTORY(ies), if they do not already exist.

       Mandatory arguments to long options are mandatory for short
       options too.

       -m, --mode=MODE
              set file mode (as in chmod), not a=rwx - umask

       -p, --parents
              no error if existing, make parent directories as needed

       -v, --verbose
              print a message for each created directory

       -Z     set SELinux security context of each created directory to
              the default type

       --context[=CTX]
              like -Z, or if CTX is specified then set the SELinux or
              SMACK security context to CTX

       --help display this help and exit

       --version
              output version information and exit

    """
    def setUp(self):
        """
        Setup function
        create test folder that is used in many tests below
        """
        self.test_dir = os.path.join(self.DEFAULT_FOLDER_PATH, "func_test")
        super(FunctionalTest, self).setUp()

    def test_mkdir(self):
        """
        Testing of creation of ONE folder
        Expectation: directory created
        """
        (exit_code, _, stderr) = MkDir().run([self.test_dir])

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)

    def test_mkdir_multiple(self):
        """
        Testing of creation of TWO folders
        Expectation: 2 directories created
        """
        dir1 = os.path.join(self.test_dir, "1")
        dir2 = os.path.join(self.test_dir, "2")
        MkDir().run([self.test_dir])

        (exit_code, _, stderr) = MkDir().run([dir1, dir2])

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(dir1),
                        "Directory 1 was not created:" + stderr)
        self.assertTrue(os.path.exists(dir2),
                        "Directory 2 was not created:" + stderr)

    def test_mode_r(self):
        """
        Create directory with mode read for user and group (using number), 
        others will NOT have permission to read
        Expectation: directory created with mode 440
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '440')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read mode with number:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40440',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_r_letter(self):
        """
        Create directory with mode read for user/group/others (using letter)
        Expectation: directory created with mode 444
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, 'r')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read mode with letter:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_w(self):
        """
        Create directory with mode write for user and others (using number), 
        group will NOT have permission to write
        Expectation: directory created with mode 202
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '202')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - write mode:" +
                         stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40202',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_x(self):
        """
        Create directory with mode execute for group and others (using number), 
        user will NOT have permission to write
        Expectation: directory created with mode 011
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '011')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation -"
                         " execute mode:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40011',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_rw(self):
        """
        Create directory with mode read/write for all (using number)
        Expectation: directory created with mode 666
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '666')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read/write mode:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40666',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_rx(self):
        """
        Create directory with mode read/execute for all (using number)
        Expectation: directory created with mode 555
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '555')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read/execute mode:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40555',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_wx(self):
        """
        Create directory with mode write/execute for all (using number)
        Expectation: directory created with mode 333
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '333')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "write/execute mode:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40333',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_rwx(self):
        """
        Create directory with mode read/write/execute for all (using number)
        Expectation: directory created with mode 777
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '777')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read/write/execute mode:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40777',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_long_r(self):
        """
        Create directory with mode read for all (using number) 
        using long argument name
        Expectation: directory created with mode 444
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE_LONG, '444')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read mode long:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def FAIL_test_mode_long_r_letter(self):
        """
        Create directory with mode read for all (using letter) 
        using long argument name.

        Findings:
        * This test fails as others will not have correct permission.
        * Using letter is problematin in mkdir command - permission for others
        are not set correctly

        Need discussion with Functional Analyst
        as r mode does not set 444 rights for a folder
        
        Expectation: directory created with mode 444
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE_LONG, 'r')]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "read mode long with letter:" + stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        s = os.stat(self.test_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_parent(self):
        """
        Create directory with parent argument
        Expectation: directory in non-existing directory
        """
        parent_dir = os.path.join(self.test_dir, "parent")
        (exit_code, _, stderr) = MkDir.run(
            [parent_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.PARENTS)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - parent:" +
                         stderr)
        self.assertTrue(os.path.exists(parent_dir),
                        "Directory was not created:" + stderr)

    def test_mkdir_parent_multiple(self):
        """
        Create multiple directories with parent argument
        Expectation: 2 directories in non-existing directory
        """
        dir1 = os.path.join(self.test_dir, "1")
        dir2 = os.path.join(self.test_dir, "2")

        (exit_code, _, stderr) = MkDir().run(
            [dir1, dir2],
            [MkDir.Arguments(MkDir.ArgumentsName.PARENTS)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(dir1),
                        "Directory 1 was not created:" + stderr)
        self.assertTrue(os.path.exists(dir2),
                        "Directory 2 was not created:" + stderr)

    def test_mkdir_parent_existing_folder(self):
        """
        Create a directory if directory exists
        Expectation: directory is not change, mkdir command exits without error
        """
        (exit_code, _, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.PARENTS)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - parent:" +
                         stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
    def test_verbose(self):
        """
        Printout details about directory creation
        Expectation: stdout provides detail information
        """
        (exit_code, stdout, stderr) = MkDir.run(
            [self.test_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.VERBOSE)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - verbose:" +
                         stderr)
        self.assertTrue(os.path.exists(self.test_dir),
                        "Directory was not created:" + stderr)
        self.assertTrue(len(stdout) > 0, "Stdout is not used for verbose:" +
                        stderr)

    def test_help(self):
        """
        Printout help about mkdir command
        Expectation: stdout provides help information
        """
        (exit_code, stdout, stderr) = MkDir.run(
            [""],
            [MkDir.Arguments(MkDir.ArgumentsName.HELP)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - help" + stderr)
        self.assertTrue(len(stdout) > 0,
                        "Stdout is not used for verbose:" + stderr)

    def test_version(self):
        """
        Printout version of mkdir command
        Expectation: stdout provides version information
        """
        (exit_code, stdout, stderr) = MkDir.run(
            [""],
            [MkDir.Arguments(MkDir.ArgumentsName.VERSION)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - help" + stderr)
        self.assertTrue(len(stdout) > 0,
                        "Stdout is not used for verbose:" + stderr)

    def test_context(self):
        '''
        Not able to test context argument as SELinux is not available

        Security-Enhanced Linux (SELinux) is a Linux kernel security module
        that provides a mechanism for supporting access control security
        policies, including mandatory access controls (MAC).
        '''
        pass

    def test_mode_r_parent(self):
        """
        Test combination of arguments
        mode read and parent
        Expectation: directory with permission 444 is created in 
        non-existing directory
        """
        parent_dir = os.path.join(self.test_dir, "parent")
        (exit_code, _, stderr) = MkDir.run(
            [parent_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '444'),
             MkDir.Arguments(MkDir.ArgumentsName.PARENTS)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation -"
                         "read mode + parent:" + stderr)
        self.assertTrue(os.path.exists(parent_dir),
                        "Parent directory was not created:" + stderr)
        s = os.stat(parent_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_r_parent_long(self):
        """
        Test combination of arguments
        mode read and parent with long names
        Expectation: directory with permission 444 is created in 
        non-existing directory
        """
        parent_dir = os.path.join(self.test_dir, "parent")
        (exit_code, _, stderr) = MkDir.run(
            [parent_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE_LONG, '444'),
             MkDir.Arguments(MkDir.ArgumentsName.PARENTS_LONG)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "long read mode + parent:" + stderr)
        self.assertTrue(os.path.exists(parent_dir),
                        "Parent directory was not created:" + stderr)
        s = os.stat(parent_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)

    def test_mode_r_parent_verbose_long(self):
        """
        Test combination of arguments
        mode read, parent and verbose with long names
        Expectation: directory with permission 444 is created in 
        non-existing directory with information on stdout
        """
        parent_dir = os.path.join(self.test_dir, "parent")
        (exit_code, stdout, stderr) = MkDir.run(
            [parent_dir],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE_LONG, '444'),
             MkDir.Arguments(MkDir.ArgumentsName.PARENTS_LONG),
             MkDir.Arguments(MkDir.ArgumentsName.VERBOSE_LONG)]
            )

        self.assertEqual(0, exit_code,
                         "Exit code raise for folder creation - "
                         "long read mode + parent + verbose:" + stderr)
        self.assertTrue(os.path.exists(parent_dir),
                        "Parent directory was not created:" + stderr)
        s = os.stat(parent_dir).st_mode
        self.assertEqual(oct(s), '0o40444',
                         "User, group, others has invalid permissions:" +
                         stderr)
        self.assertTrue(len(stdout) > 0, "Stdout is not used for verbose:" +
                        stderr)
