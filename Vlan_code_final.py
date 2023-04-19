import telnetlib
import time

host = '10.10.1.5'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"create vlan it_network\n")
tn.write(b"configure vlan it_network tag 100\n")
tn.write(b"configure vlan it_network add port 2 untagged\n")
tn.write(b"configure vlan it_network add port 1 tagged\n")
tn.write(b"configure vlan default delete ports all\n")
tn.write(b"configure it_network ipaddress 10.10.1.30/24\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#mgmt_network switch
host = "10.10.1.6"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"create vlan mgmt_network\n")
tn.write(b"configure vlan mgmt_network tag 200\n")
tn.write(b"configure vlan mgmt_network add port 2 untagged\n")
tn.write(b"configure vlan mgmt_network add port 1 tagged\n")
tn.write(b"configure vlan default delete ports all\n")
tn.write(b"configure mgmt_network ipaddress 10.10.1.31/24\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#acct_network switch
host = "10.10.1.7"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"create vlan acct_network\n")
tn.write(b"configure vlan acct_network tag 300\n")
tn.write(b"configure vlan acct_network add port 2 untagged\n")
tn.write(b"configure vlan acct_network add port 1 tagged\n")
tn.write(b"configure vlan default delete ports all\n")
tn.write(b"configure acct_network ipaddress 10.10.1.32/24\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#user_network switch
host = "10.10.1.8"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"create vlan user_network\n")
tn.write(b"configure vlan user_network tag 400\n")
tn.write(b"configure vlan user_network add port 2 untagged\n")
tn.write(b"configure vlan user_network add port 3 untagged\n")
tn.write(b"configure vlan user_network add port 4 untagged\n")
tn.write(b"configure vlan user_network add port 5 untagged\n")
tn.write(b"configure user_network add port 1 tagged\n")
tn.write(b"configure vlan default delete ports all\n")
tn.write(b"configure user_network ipaddress 10.10.1.22/24\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#local switch
host = "10.10.1.2"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"create vlan it_network\n")
tn.write(b"create vlan mgmt_network\n")
tn.write(b"create vlan acct_network\n")
tn.write(b"create vlan user_network\n")
tn.write(b"configure vlan it_network tag 100\n")
tn.write(b"configure vlan mgmt_network tag 200\n")
tn.write(b"configure vlan acct_network tag 300\n")
tn.write(b"configure vlan user_network tag 400\n")
tn.write(b"configure it_network add port 3 tagged\n")
tn.write(b"configure mgmt_network add port 5 tagged\n")
tn.write(b"configure acct_network add port 7 tagged\n")
tn.write(b"configure user_network add port 9 tagged\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

tn.close()
