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


#for device in nw_device_list:
#    for attribs in device.interface:
#        if_name = attribs['interface']
#        if_ip = attribs['ip_address']
#        if_submask = attribs['subnet_mask']
#        if_route_p = attribs['route_protocol']
#        print(device.name, if_name, if_ip, if_submask, if_route_p)
        #device.deploy_config(if_name, if_ip, if_submask, if_route_p)

#intf_update = conn.send_configs(["interface GigabitEthernet2", "ip address 10.100.12.1 255.255.255.0", "no shutdown"])

#print(intf_update.result)
#show_run = conn.send_command("show run")
#print(show_run.result)