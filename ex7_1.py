#Description: How to display all unused ports from 1 - 200 in a SERVICES file
import pickle
import re
import sys
if sys.platform == 'win32':
    file = r"C:\WINDOWS\system32\drivers\etc\services"
else:
    file = r"/etc/services"


all_ports = set()
print(all_ports)
used_ports = set()

with open(file, mode='rt') as fh_in :
    for line in fh_in :
        m = re.search(r'(\d+)/(tcp|udp)', line) # 2 groups gets port number which has tcp or udp
        if m:# 1 or more digits
            print(m)
            #print(m.group(1))
            port = int(m.group(1))# convert to int
            all_ports.add(port)
            if port < 200:
                used_ports.add(int(m.group(1)))

print(f"Used Ports: {used_ports}" )
print(f"All Ports: {all_ports}" )
print(f"Unused Ports: {all_ports - used_ports}" )
