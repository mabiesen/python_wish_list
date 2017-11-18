## relevant websites
## https://medium.com/capital-one-developers/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989
## http://www.mervine.net/executing-bash-from-python

## this lib should:
## 1. Execute commands and return output
## 2. Execute commands no output
## 3. Identify processes

## NOTE:  psutil not properly installing in cygwin, removed for now

import subprocess
import os

class BashClass:

    def __init__(self):
        print("bash helper initialized")

    def run_commands_from_list(self, commandlist):
        ## open file, read and execute line by line, return output
        returnlist = []
        for i in commandlist:
            returnlist.append(self.run_bash_command(i))
        return returnlist

    def run_bash_command(self, bashCommand):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if len(output) < 1:
            output = "none"
        return output

    def script_directory_path(self):
        mypath = os.path.dirname(os.path.realpath(__file__))
        return mypath

    def all_directory_files(self, directory):
        filelist = []
        for filename in os.listdir(directory):
            full_filepath = os.path.join(directory, filename)
            filelist.append(full_filepath)
        return filelist

    def destroy_file(self, fullfilename):
        os.remove(fullfilename)


    ## check if file exists


    ## check if directory exists



## Kept this separate as best practice
'''
There are two best practices to follow when using this method:
Catch the exception (WindowsError, OSError) on invalid path. If the exception is thrown, do not perform any recursive operations, especially destructive ones. They will operate on the old path and not the new one.
Return to your old directory when you're done. This can be done in an exception-safe manner by wrapping your chdir call in a context manager, like Brian M. Hunt did in his answer.
Changing the current working directory in a subprocess does not change the current working directory in the parent process. This is true of the Python interpreter as well. You cannot use os.chdir() to change the CWD of the calling process.
'''
class ChangeDirClass:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
