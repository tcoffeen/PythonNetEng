import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('172.16.128.72', 'tom', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent=4))

iosvl2.close()
