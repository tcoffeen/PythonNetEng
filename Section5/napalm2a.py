import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('172.16.128.72', 'tom', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()
