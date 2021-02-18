import nmap3
import subprocess
import sys
from pprint import pprint

nmap = nmap3.Nmap()

target = subprocess.check_output("nmap --iflist | grep DST/MASK -A1 | grep -vE '(DST)' | awk '{print $1}'", shell=True, universal_newlines=True)
print("Your network is: " + target[:-1])

options = ['Scan Top Ports', 'List Scan', 'OS Detection']
print("NMAP options: 1)" + options[0] + ", 2)" + options[1] + ", 3)" + options[2])
choice = input("Please, choose one of NMAP options: ")

if  choice == '1':
    print("Running NMAP Scan Top Ports...")
    top_ports = nmap.scan_top_ports(target[:-1])
    pprint(top_ports)

if  choice == '2':
    print("Running NMAP List Scan...")
    list_scan = nmap.nmap_list_scan(target[:-1])
    pprint(list_scan)

if  choice == '3':
    print("Running NMAP OS Detection...")
    os_detection = nmap.nmap_os_detection(target[:-1])
    pprint(os_detection)

else:
    print("is not a valid network/domain!")

print("Task finished!")