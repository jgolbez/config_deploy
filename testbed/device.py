# Imports

from scrapli import Scrapli






class Device:
    def __init__(self, device, interface_list):
        self.name = device
        self.interface = interface_list


    def build_intf_config(self):
        self.config_str = ''
        for attrib in self.interface:
            self.if_name = attrib['interface']
            self.if_ip = attrib['ip_address']
            self.if_submask = attrib['subnet_mask']
            self.if_rp = attrib['route_protocol']
            self.config_str += f"interface {self.if_name}\nip address {self.if_ip} {self.if_submask}\nno shutdown\n"


    def deploy_intf_config(self):
        device = {
            "host": self.name,
            "auth_username": "admin",
            "auth_password": "admin",
            "platform": "cisco_iosxe"
        }
        conn = Scrapli(**device)
        conn.open()
        intf_update = conn.send_config(self.config_str)
        intf_update.raise_for_status()
        print(intf_update)


