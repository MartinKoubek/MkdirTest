"""
Helper function for mkdir command

It is big benefit to hide (wrap) calling mkdir command to a class as:
in case of interface change, program change, only this 
class can be changed/extended

Created on Jun 17, 2021
@author: Martin Koubek
"""
import subprocess


class MkDir(object):
    """
    Command -  mkdir - it can be used also out of wrapper for some 
    special tests
    """
    COMMAND = "mkdir"

    class ArgumentsName():
        """
        List of arguments for mkdir command
        
        Arguments SHALL NOT be called directly from unittests, but shall be
        called over "abstraction" class that helps to maintain code more easily 
        when argument may be changed in next release 
        """
        MODE = "-m="
        MODE_LONG = "--mode="
        PARENTS = "-p"
        PARENTS_LONG = "--parents"
        VERBOSE = "-v"
        VERBOSE_LONG = "--verbose"
        SEC_CONTEXT = "-Z"
        CONTEXT = "--context="
        HELP = "--help"
        VERSION = "--version"
        INVALID_ARG = "--invalid"

    class Arguments():
        """
        This class helps to build final command for mkdir
        
        Example of usage:
        * ArgumentsName::MODE, 'rwx'
        * ArgumentsName::PARENTS
        """
        def __init__(self, arguemnt_name, argument_value=""):
            self.name = arguemnt_name
            self.value = argument_value

    @staticmethod
    def run(directory_list, arguments_list=[]):
        """
        This is a static method that run mkdir command.
        
        inputs:
        directory_list - list of strings is expected
        arguments_list - list of Arguments is expected
        
        outputs:
        exit_code - exit code of mkdir command
        stdout - stdout from mkdir command
        stderr - stderr from mkdir command
        
        Example of use:
        MkDir.run(
            ["directory_path_name"],
            [MkDir.Arguments(MkDir.ArgumentsName.MODE, '440')]
            )
            
        MkDir.run(
            ["directory_path_name_1", "directory_path_name_2"],
            [MkDir.Arguments(MkDir.ArgumentsName.PARENTS]
            )
        """
        if not isinstance(directory_list, list):
            return ("Directories list is not a list", None, None)
        
        if not isinstance(arguments_list, list):
            return ("Arguments list is not a list", None, None)

        command = [MkDir().COMMAND]
        command.extend(directory_list)
        for arguments in arguments_list:
            if not isinstance(arguments, MkDir.Arguments):
                return ("Arguments are not valid type", None, None)

            command.append(arguments.name + arguments.value)

        proc = subprocess.run(command,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

        exit_code = proc.returncode
        stdout = proc.stdout.decode()
        stderr = proc.stderr.decode()
        return (exit_code, stdout, stderr)
