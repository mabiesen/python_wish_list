import paramiko
import scp

class RemoteGetPutClass:

    myserver = ''
    myport = ''
    myuname = ''
    mypswd = ''

    def _init_(self,server, port, uname, pswd):
        print('remote helper initiated')
        self.myserver = server
        self.myport = port
        self.myuname = uname
        self.mypswd = pswd


    def create_ssh_client(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(self.server, self.port, self.user, self.password)
        except e:
            print("Connection not obtained because....")
            print(e)
            print(" ")
        return client

    def create_transport():
        ssh = create_ssh_client(self.myserver, self.myport, self.myuname, self.pswd)
        myscp = scp.SCPClient(ssh.get_transport())
        return myscp

    def get_file(fullFilePath):
        myscp = create_transport()
        try:
            myscp.get(fullFilePath)
        except e:
            print("Unable to get file because....")
            print(e)
            print(" ")
        myscp.close()

    def get_files(filePathList):
        myscp = create_transport()
        for f in filePathList:
            try:
                myscp.get(f)
            except:
                print("get_file not completed for: " + f)
        print("Done getting files")
        print(" ")
        myscp.close()

    def put_file(localFilePath,remoteFilepath):
        myscp = create_transport()
        try:
            myscp.put(localFilePath, remoteFilepath)
        except e:
            print("Unable to put file because....")
            print(e)
            print(" ")
        myscp.close()

    def put_files(filePathList):
        for f in filePathList:
            try:
                put_file(f)
            except:
                print("put_file not completed for: " + f)
        print("Done putting files")
        print(" ")
