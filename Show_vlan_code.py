import getpass
import sys
import telnetlib

HOST = "10.10.1.30"
user = input("Enter your Telnet username: ")
password = getpass.getpass()


tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write("admin\n")
if password:
    tn.read_until("Password: ")
    tn.write("\n"

tn.write(b"show vlan\n")

output = tn.read_until(b"# ")
output_lines = output.decode('ascii').splitlines()
vlans = []
for line in output_lines[1:]:
    vlan_id = line.split()[0]
    if vlan_id.isdigit():
        vlans.append(int(vlan_id))


print("Existing VLANs:", vlans)

tn.write("exit\n")
tn.write("y\n")
