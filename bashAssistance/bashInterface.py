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
    
    ## NOTE:  FTP did not work, try with scp, did not work so tried with paramiko, did not work
    ## DOES NOT WORK
    def scp_file(self,username,pswd, files, remotepath, localpath='./', server='local'):
        paramiko.util.log_to_file('/tmp/paramiko.log')
        paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

        files = []

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
                    paramiko.AutoAddPolicy())
        ssh.connect(server, username=username, password=pswd)
        sftp = ssh.open_sftp()

        for file in files:
            file_remote = remotepath + file
            file_local = localpath + file

            print file_remote + '>>>' + file_local

            sftp.get(file_remote, file_local)

        sftp.close()
        ssh.close()
