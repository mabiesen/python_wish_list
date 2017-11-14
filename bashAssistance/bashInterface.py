## relevant websites
## https://medium.com/capital-one-developers/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989
## http://www.mervine.net/executing-bash-from-python

## this lib should:
## 1. Execute commands and return output
## 2. Execute commands no output
## 3. Identify processes

import subprocess
import psutil
import os

class BashHelper:

    def __init__():
        print("bash helper initialized")

    def runCommandsFromListReturnOutput(commandlist):
        ## open file, read and execute line by line, return output
        returnlist = []
        for i in commandlist:
            returnlist.append(self.runBashCommand(i))
        return returnlist
        
    def runBashCommand(bashCommand):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if len(output) < 1:
            output = "none"
        return output

    def killProcess(pidfile_path):
        try:
            pid = int(pidfile_path.read_text())
        except FileNotFoundError:
            print("Process file does not exist")
            return
        except ValueError:
            print("Invalid input")

        try:
            proc=psutil.Process(pid)
            print("Killing", proc.name())
            proc.kill()
        except psutil.NoSuchProcess as ex:
            print("No such process")
            
    def script_directory_path():
        mypath = os.path.dirname(os.path.realpath(__file__))
        return mypath
    
    def all_directory_files(directory):
        filelist = []
        for filename in os.listdir(directory):
            full_filepath = os.path.join(directory, filename)
            filelist.append(full_filepath)
        return filelist
    
    def destroy_file(filename):
        os.remove(filename)

