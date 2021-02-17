import nmap3
import subprocess
import sys
from pprint import pprint

nmap = nmap3.Nmap()

target = subprocess.check_output("nmap --iflist | grep DST/MASK -A1 | grep -vE '(DST)' | awk '{print $1}'", shell=True, universal_newlines=True)
print("Your network is: " + target[:-1])

options = {'top_ports': 'scan_top_ports', 'list_scan': 'nmap_list_scan', 'os_detection': 'nmap_os_detection'}
print("NMAP options: A)" + options['top_ports'] + ", B)" + options['list_scan'] + ", C)" + options['os_detection'])
choice = input("Please, choose one of NMAP options: ")

if choice == 'A' or 'a':
    print("Running NMAP Scan Top Ports...")
    top_ports = nmap.scan_top_ports(target[:-1])
    pprint(top_ports)

elif choice == 'B' or 'b':
    print("Running NMAP List Scan...")
    list_scan = nmap.nmap_list_scan(target[:-1])
    pprint(list_scan)

elif choice == 'C' or 'c':
    print("Running NMAP OS Detection...")
    os_detection = nmap.nmap_os_detection(target[:-1])
    pprint(os_detection)

else:
    print("is not a valid network/domain!")

print("Task finished!")