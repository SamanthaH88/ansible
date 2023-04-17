import getpass
import telnetlib

HOST = "10.10.1.5"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("show vlan\n")
tn.write("exit\n")

print tn.read_all()