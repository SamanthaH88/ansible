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

tn.write(b'disable clipaging\n')
tn.write(b'show vlan\n')
output =tn.read_until(b'Total number of Vlans(s) :', time out=5)
print(output.decode('ascii'))
tn.write(b'exit\n')
time.sleep(1)

host = '10.10.1.6'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b'disable clipaging\n')
tn.write(b'show vlan\n')
output =tn.read_until(b'Total number of Vlans(s) :', time out=5)
print(output.decode('ascii'))
tn.write(b'exit\n')
time.sleep(1)

host = '10.10.1.7'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b'disable clipaging\n')
tn.write(b'show vlan\n')
output =tn.read_until(b'Total number of Vlans(s) :', time out=5)
print(output.decode('ascii'))
tn.write(b'exit\n')
time.sleep(1)

host = '10.10.1.8'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b'disable clipaging\n')
tn.write(b'show vlan\n')
output =tn.read_until(b'Total number of Vlans(s) :', time out=5)
print(output.decode('ascii'))
tn.write(b'exit\n')
time.sleep(1)

host = '10.10.1.2'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b'disable clipaging\n')
tn.write(b'show vlan\n')
output =tn.read_until(b'Total number of Vlans(s) :', time out=5)
print(output.decode('ascii'))
tn.write(b'exit\n')
time.sleep(1)

tn.close()
