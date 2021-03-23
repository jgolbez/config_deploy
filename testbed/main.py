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
    nw_device_list.append(nw_device)

for device in nw_device_list:
    device.build_intf_config()
    print(device.config_str)
    device.deploy_intf_config()
