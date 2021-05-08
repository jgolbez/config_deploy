from scrapli import Scrapli
from scrapli.exceptions import ScrapliTimeout, ScrapliAuthenticationFailed

from data_file import create_records
from device import Device

# Data Sources
data_source = create_records()

# Create objects based on data source
nw_device_list = []
for device in data_source.keys():
    nw_device_list.append(device)

print(nw_device_list)
for nw_device in nw_device_list:
    device = {
                "host": nw_device,
                "auth_username": "admin",
                "auth_password": "admin",
                "auth_strict_key": False,
                "platform": "cisco_iosxe",
                "timeout_transport": 20,
                "timeout_socket": 20,
                "timeout_ops": 20

            }
    conn = Scrapli(**device)
    try:
        conn.open()
        # reset_cfg_list = ["write erase", "\n\n", "copy bootflash:nw_auto_reset.cfg start", "\n\n", "reload in 1", "\n\n"]
        reset_cfg_string = "write erase\n\ncopy bootflash:nw_auto_reset.cfg start\n\nreload in 1\n\n"
        reset_cfg = conn.send_command(reset_cfg_string)
        conn.close()
    except ScrapliTimeout:
        print(f"Cannot reach {device['host']}")
        pass
    except ScrapliAuthenticationFailed:
        print(f"Cannot reach {device['host']}")
        pass



