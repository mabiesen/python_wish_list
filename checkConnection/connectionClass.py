import python-nmap
import socket
import os

class ConnectionClass:

    local_ip = ''

    def _init_(self):
        print("Initiating connection class")
        self.local_ip=socket.gethostbyname(socket.gethostname())

    def print_local_ip(self):
        print(self.local_ip)

    def scan_ip_port_range_tcp(self, this_ip, port_range='0-65535'):
        nm = nmap.PortScanner()
        nm.scan(this_ip, port_range)
        nm[this_ip].all_protocols()     # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
        if ('tcp' in nm[this_ip]):
            print("Found tcp ports!")
            return list(nm[this_ip]['tcp'].keys())
        else:
            print("Found no TCP ports,return None")
            return None

    def get_tcp_port_state(self, hostname, port):
        return nm[hostname]['tcp'][port]['state']

    def print_os_info(self,hostname):
        print('----------------------------------------------------')
        # Os detection (need root privileges)
        nm.scan(hostname, arguments="-O")
        if nm[hostname].has_key('osclass'):
            for osclass in nm[hostname]['osclass']:
                print('OsClass.type : {0}'.format(osclass['type']))
                print('OsClass.vendor : {0}'.format(osclass['vendor']))
                print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                print('OsClass.osgen : {0}'.format(osclass['osgen']))
                print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                print('')

        if nm[hostname].has_key('osmatch'):
            for osmatch in nm['127.0.0.1']['osmatch']:
                print('osmatch.name : {0}'.format(osmatch['name']))
                print('osmatch.accuracy : {0}'.format(osmatch['accuracy']))
                print('osmatch.line : {0}'.format(osmatch['line']))
                print('')

        if nm[hostname].has_key('fingerprint'):
            print('Fingerprint : {0}'.format(nm[hostname]['fingerprint']))

    def ping_ip(self,hostname):
        response = os.system("ping -c 1 " + hostname)
        if response:
            return response
        else:
            return "none"
