# Imports

from data_file import create_records
from device import Device

# Data Sources
data_source = create_records()
print(data_source)

# Main Loop

# Create objects based on data source
nw_device_list = []
for device, record in data_source.items():
    nw_device = Device(device, record)
    print(nw_device.name)
    nw_device_list.append(nw_device)
print(nw_device_list)
for device in nw_device_list:
    print(device.name)
    device.build_config()
    print(device.config_str)
    device.deploy_config()

# Testing for VRF Output
#for device in nw_device_list:
#    device.verify_vrf()
