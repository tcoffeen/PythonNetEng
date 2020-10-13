import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosv = driver('172.16.128.72', 'tom', 'cisco')
iosv.open()

ios_output = iosv.get_bgp_neighbors()
print (json.dumps(ios_output, indent=4))

iosv.close()

