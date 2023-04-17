import telnetlib
import time

host = '10.10.1.5'
port = '23'
user = 'service'
password = 'password'

tn = telnetli.Yelnet(host=host, port=port)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'terminal length 0\n')
tn.write(b'show vlan\n')
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all()
output = output.decode()
print(output)