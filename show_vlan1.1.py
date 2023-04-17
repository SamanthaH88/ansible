import getpass
import telnetlib


HOST = "10.10.1.30"
user = input("Enter your Telnet username: ")
password = getpass.getpass()


tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"show vlan\n")

output = tn.read_until(b"# ", timeout=5)
output_lines = output.decode('ascii').splitlines()
vlans = []
for line in output_lines[1:]:
    vlan_id = line.split()[0]
    if vlan_id.isdigit():
        vlans.append(int(vlan_id))

print("Existing VLANs:", vlans)

tn.write(b"exit\n")
tn.close()
