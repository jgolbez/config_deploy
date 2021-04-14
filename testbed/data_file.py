# Imports

import pyexcel
from collections import defaultdict

# Data Sources
sheet = pyexcel.get_sheet(file_name="lab_nw_auto_test.xlsx", name_columns_by_row=0)


# Function

#Dmitry helped me with this
def create_records():
    # DefaultDict creates an 'empty' dict we can append lists to without having to create ahead, accepts value w/ no key
    # Instead supplies a 'default' key based on the type (here list)
    device_to_interfaces = defaultdict(list)
    for record in sheet.records:
        # Pop drops the column specified after grabbing the detail of it and assigning it to device
        device = record.pop("device")
        # Take the rest of the row and convert it directly to a dict
        interface_data = dict(record)
        # Now append that dict to the default dict using a key of device
        device_to_interfaces[device].append(interface_data)
        print(device_to_interfaces)

    return dict(device_to_interfaces)
