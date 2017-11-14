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
import pexpect

class BashHelper:

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
        
    def scp_multiple_files(self, filelist, ipaddr, user, password):
        for i in filelist:
            self.scp_file(i, ipaddr, user, password)
    
    ## NOTE:  FTP did not work, try with scp
    def scp_file(self, fullfilepath, ipaddr, user, password):
        filename, filedir = os.path.split(fullfilepath)
        child = pexpect.spawn ('ftp ' + ipaddr)
        child.expect ("User " + "(" + ipaddr + ":(none)):")
        child.sendline (user)
        child.expect ('Password:')
        child.sendline (password)
        child.expect ('ftp> ')
        child.sendline ('cd ' + filedir)
        child.expect('ftp> ')
        child.sendline ('get ' + filename)
        child.expect('ftp> ')
        child.sendline ('bye')
