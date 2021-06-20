"""
Interface Testing 
is defined as a software testing type which verifies whether input and output 
of software system is is done correctly.

Testing was devided to:
* Character encoding - special chars, UTF-8, UTF-16
* Extra long name directories
* Invalid parameters

Created on Jun 17, 2021
@author: Martin Koubek
"""
import os

from test_cases.base_test import BaseTest
from helper.mkdir import MkDir


class InterfaceTest(BaseTest):
    '''
    https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/

    Following are general rules for both Linux, and Unix (including *BSD)
    like systems:

    All file names are case sensitive. So filename vivek.txt Vivek.txt 
    VIVEK.txt all are three different files.
    You can use upper and lowercase letters, numbers, “.” (dot), and “_” 
    (underscore) symbols.
    You can use other special characters such as blank space, but they are hard
    to use and it is better to avoid them.
    In short, filenames may contain any character except / (root directory), 
    which is reserved as the separator between files and directories in a 
    pathname. You cannot use the null character.
    No need to use . (dot) in a filename. Some time dot improves readability of 
    filenames. And you can use dot based filename extension to identify file. 
    For example:

    .sh = Shell file
    .tar.gz = Compressed archive

    Most modern Linux and UNIX limit filename to 255 characters (255 bytes). 
    However, some older version of UNIX system limits filenames to 14 
    characters only.
    A filename must be unique inside its directory. For example, inside 
    /home/vivek directory you cannot create a demo.txt file and demo.txt 
    directory name. However, other directory may have files with the same 
    names. For example, you can create demo.txt directory in /tmp.
    Linux / UNIX: Reserved Characters And Words
    
    Avoid using the following characters from appearing in file names:

        /
        >
        |
        :
        &

    Please note that Linux and UNIX allows white 
    spaces, , |, \, :, (, ), &, ;, as well as wildcards such as ? 
    and *, to be quoted or escaped using \ symbol. 
    '''

    def test_mkdir_special_chars(self):
        """
        Test if a directory is created with special chars
        Expectation: directory created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, r"# |\:()&;/")
        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(0, exit_code, 
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(
            os.path.exists(directory),
             "Directory was not created:" + stderr)

    def test_mkdir_utf8(self):
        """
        Test if a directory is created with special chars - utf8
        Expectation: directory created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "+ěščřžýáíéú")
        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(0, exit_code, 
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(directory),
                        "Directory was not created:" + stderr)

    def test_mkdir_utf16(self):
        """
        Test if a directory is created with special chars - utf16
        Expectation: directory created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "𐐷")
        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(0, exit_code, 
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(directory),
                         "Directory was not created:" + stderr)

    def test_mkdir_name_w_255_chars(self):
        """
        Test if a directory is created with 255 chars of directory name
        Expectation: directory created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "".join(['a']*255))
        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(0, exit_code, 
                         "Exit code raise for folder creation:" + stderr)
        self.assertTrue(os.path.exists(directory),
                        "Directory was not created:" + stderr)

    def test_mkdir_name_w_256_chars(self):
        """
        Test if a directory is created with 256 chars of directory name
        Expectation: directory NOT created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "".join(['a']*256))
        (exit_code, _, stderr) = MkDir().run([directory])

        self.assertEqual(1, exit_code, 
                         "Exit code did not raise for folder creation:" +
                         stderr)
        self.assertFalse(os.path.exists(directory),
                        "Directory was not created:" + stderr)

    def test_mode_invalid_letter(self):
        """
        Test if a directory is created with invalid mode letter
        Expectation: directory NOT created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        (exit_code, _, stderr) = MkDir.run([directory], 
                        [MkDir.Arguments(MkDir.ArgumentsName.MODE, 'a')])

        self.assertEqual(1, exit_code, "Exit code raise for folder creation - "
                         "read mode with number:" + stderr)
        self.assertFalse(os.path.exists(directory), 
                         "Directory was not created:" + stderr)

    def test_mode_invalid_number(self):
        """
        Test if a directory is created with invalid mode number
        Expectation: directory NOT created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH, "test")
        (exit_code, _, stderr) = MkDir.run([directory], 
                        [MkDir.Arguments(MkDir.ArgumentsName.MODE, '888')])

        self.assertEqual(1, exit_code, "Exit code raise for folder creation - "
                         "read mode with number:" + stderr)
        self.assertFalse(os.path.exists(directory), 
                         "Directory was not created:" + stderr)

    def test_invalid_argument(self):
        """
        Test if a directory is created if provided argument is invalid
        Expectation: directory NOT created
        """
        directory = os.path.join(self.DEFAULT_FOLDER_PATH,"test")
        (exit_code, _, stderr) = MkDir.run([directory], 
                        [MkDir.Arguments(MkDir.ArgumentsName.INVALID_ARG)])

        self.assertEqual(1, exit_code, "Exit code raise for folder creation - "
                         "read mode with number:" + stderr)
        self.assertFalse(os.path.exists(directory), 
                         "Directory was not created:" + stderr)

    def test_mkdir_255_dirs(self):
        """
        Test if 255  directories are created in one command
        Expectation: directory created
        """
        max_num_directories = 255
        dir_list = []
        for idx in range (max_num_directories):
            dir_list.append(os.path.join(self.DEFAULT_FOLDER_PATH,'test_' +
                                         str(idx)))
        (exit_code, _, stderr) = MkDir().run(dir_list)

        self.assertEqual(0, exit_code, 
                         "Exit code raise for folder creation:" + stderr)
        for directory in dir_list:
            self.assertTrue(os.path.exists(directory),
                            "Directory was not created:" + stderr)
