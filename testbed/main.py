# Imports
import data_file
import time
from data_file import create_records
from device import Device

# Data Sources
data_source = create_records()
print(data_source)
ping_list = data_file.create_verify_records()
print(ping_list)

# Main Loop

# Create objects based on data source
nw_device_list = []
for device, record in data_source.items():
    nw_device = Device(device, record)
    nw_device_list.append(nw_device)
for device in nw_device_list:
    print(device.name)
    device.build_config()
    print(device.config_str)
    device.deploy_config()
time.sleep(45)
for device in nw_device_list:
    device.verify_ping(ping_list)
    device.verify_routing()

# Testing for VRF Output
#for device in nw_device_list:
#    device.verify_vrf()
