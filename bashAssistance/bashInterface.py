## relevant websites
## https://medium.com/capital-one-developers/bashing-the-bash-replacing-shell-scripts-with-python-d8d201bc0989
## http://www.mervine.net/executing-bash-from-python

import subprocess
import psutil

class BashHelper:

    def __init__():
        print("bash helper initialized")

    def runCommandsFromFileReturnOutput(fileWithCommands):
        ## open file, read and execute line by line, return output
        
    def runBashCommand(bashCommand):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
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

