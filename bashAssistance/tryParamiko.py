import paramiko

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.1.78', 22, 'pi', 'raspberry')
scp = SCPClient(ssh.get_transport())
