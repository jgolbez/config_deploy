# Imports

from scrapli import Scrapli
from scrapli.helper import textfsm_parse

class Device:
    def __init__(self, device, attrib_list):
        self.name = device
        self.attrib_list = attrib_list
#        self.vrf = interface_list
        self.ospf_process_cfg = False
        self.eigrp_process_cfg = False
        self.bgp_process_cfg = False


    def build_config(self):
        self.config_str = ''
        for attrib in self.attrib_list:
            self.if_name = attrib['interface']
            self.if_ip = attrib['ip_address']
            self.if_submask = attrib['subnet_mask']
            self.if_rp = attrib['route_protocol']
            self.ospf_pid = attrib['ospf_process']
            self.ospf_area = attrib['ospf_area']
            self.ospf_nw_type = attrib['ospf_nw_type']
            self.eigrp_process = attrib['eigrp_process']
            self.eigrp_af = attrib['eigrp_af']
            self.eigrp_asnum = attrib['eigrp_asnum']
            self.eigrp_network = attrib['eigrp_network']
            self.bgp_process = attrib['bgp_process']
            self.bgp_af = attrib['bgp_af']
            self.bgp_neighbor = attrib['bgp_neighbor']
            self.bgp_nw_prefix = attrib['bgp_nw_prefix']
            self.bgp_nw_mask = attrib['bgp_nw_mask']
            self.bgp_remote_as = attrib['bgp_remote_as']
            self.config_str += f"interface {self.if_name}\nip address {self.if_ip} {self.if_submask}\nno shutdown\n"
            if self.if_rp == "ospf":
                self.config_str += f"ip ospf {self.ospf_pid} area {self.ospf_area}\nip ospf network {self.ospf_nw_type}\n"
                if not self.ospf_process_cfg:
                    self.config_str += f"router ospf {self.ospf_pid}\n"
                    self.ospf_process_cfg = True
            if self.if_rp == "eigrp":
                    self.config_str += f"router eigrp {self.eigrp_process}\naddress-family {self.eigrp_af} autonomous-system {self.eigrp_asnum}\n"
                    self.config_str += f"network {self.if_ip} 0.0.0.0\n"
            if self.if_rp == "bgp":
                self.config_str += f"router bgp {self.bgp_process}\naddress-family {self.bgp_af}\n "
                if self.bgp_neighbor != '':
                    self.config_str += f"neighbor {self.bgp_neighbor} remote-as {self.bgp_remote_as}\n"
                else:
                    pass
                if self.bgp_nw_prefix == '':
                    pass
                elif self.bgp_nw_prefix != '':
                    self.config_str += f"network {self.bgp_nw_prefix} mask {self.bgp_nw_mask}\n "

    #            self.deploy_config()
#            elif self.if_rp == "eigrp":
#                self.config_str += f""
#            elif self.if_rp == "bgp":



    def deploy_config(self):
        device = {
            "host": self.name,
            "auth_username": "admin",
            "auth_password": "admin",
            "platform": "cisco_iosxe"
        }
        conn = Scrapli(**device)
        conn.open()
        cfg_update = conn.send_config(self.config_str)
        cfg_update.raise_for_status()
        print(cfg_update)

    def verify_vrf(self):
        output_list = []
        device = {
            "host": self.name,
            "auth_username": "admin",
            "auth_password": "admin",
            "platform": "cisco_iosxe"

        }
        conn = Scrapli(**device)
        conn.open()
        verify_vrf_cfg = conn.send_command("show vrf")
        verify_vrf_cfg.raise_for_status()
        print(verify_vrf_cfg.result)
        structure_result = verify_vrf_cfg.genie_parse_output()
        #structure_result = textfsm_parse("cisco_ios_show_vrf.textfsm", verify_vrf_cfg.result)
        print(structure_result)
        #self.vrf_list = output_list
        #print(output_list)
        #print(self.vrf_list)


#        output_list.append(verify_vrf_cfg.result.split("\n"))
#        print(output_list)#

