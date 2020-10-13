import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('172.16.128.72', 'tom', 'cisco')
iosvl2.open()

bgp_neighbors = iosvl2.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

iosvl2.close()
