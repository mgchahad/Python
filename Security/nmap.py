import nmap3
import subprocess
import sys
from pprint import pprint

nmap = nmap3.Nmap()

target = subprocess.check_output("nmap --iflist | grep DST/MASK -A1 | grep -vE '(DST)' | awk '{print $1}'", shell=True, universal_newlines=True)
print("\nRunning selected task on: ")
print(target[:-1])

if target:
    top_ports = nmap.scan_top_ports(target[:-1])
    pprint(top_ports)
if target:
    list_scan = nmap.nmap_list_scan(target[:-1])
    pprint(list_scan)
if target:
    os_detection = nmap.nmap_os_detection(target[:-1])
    pprint(os_detection)
else:
    print("is not a valid network/domain!")

print("Task finished!")
