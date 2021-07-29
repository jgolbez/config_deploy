# Import Section
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


testdict = {
  "deviceType": [
    "vedge-CSR-1000v"
  ],
  "templateMinVersion": "15.0.0",
  "templateType": "cisco_vpn_interface",
  "lastUpdatedBy": "admin",
  "editedTemplateDefinition": {
    "if-name": {
      "vipObjectType": "object",
      "vipType": "variableName",
      "vipValue": "",
      "vipVariableName": "WAN_MPLS_PHYS_INTF"
    },
    "description": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_description"
    },
    "ip": {
      "address": {
        "vipObjectType": "object",
        "vipType": "variableName",
        "vipValue": "",
        "vipVariableName": "WAN_MPLS_IP_ADDR"
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "dhcp-helper": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_dhcp_helper"
    },
    "flow-control": {},
    "clear-dont-fragment": {},
    "pmtu": {},
    "mtu": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1500,
      "vipVariableName": "vpn_if_ip_mtu"
    },
    "static-ingress-qos": {},
    "tcp-mss-adjust": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tcp_mss_adjust"
    },
    "mac-address": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_mac_address"
    },
    "speed": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_speed"
    },
    "duplex": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_duplex"
    },
    "shutdown": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "false",
      "vipVariableName": "vpn_if_shutdown"
    },
    "arp-timeout": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1200,
      "vipVariableName": "vpn_if_arp_timeout"
    },
    "autonegotiate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "true",
      "vipVariableName": "vpn_if_autonegotiate"
    },
    "shaping-rate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "rewrite_shaping_rate"
    },
    "qos-map": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "qos_map"
    },
    "tracker": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tracker"
    },
    "bandwidth-upstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_upstream"
    },
    "bandwidth-downstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_downstream"
    },
    "block-non-source-ip": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "false",
      "vipVariableName": "vpn_if_block_non_source_ip"
    },
    "rewrite-rule": {
      "rule-name": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "rewrite_rule_name"
      }
    },
    "tloc-extension": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tloc_extension"
    },
    "load-interval": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 30,
      "vipVariableName": "vpn_if_load_interval"
    },
    "icmp-redirect-disable": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "true",
      "vipVariableName": "vpn_if_icmp_redirect_disable"
    },
    "tloc-extension-gre-from": {
      "src-ip": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_src_ip"
      },
      "xconnect": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_xconnect"
      }
    },
    "access-list": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "direction"
      ]
    },
    "tunnel-interface": {
      "encapsulation": {
        "vipType": "constant",
        "vipValue": [
          {
            "preference": {
              "vipObjectType": "object",
              "vipType": "ignore",
              "vipVariableName": "vpn_if_tunnel_ipsec_preference"
            },
            "weight": {
              "vipObjectType": "object",
              "vipType": "ignore",
              "vipValue": 1,
              "vipVariableName": "vpn_if_tunnel_ipsec_weight"
            },
            "encap": {
              "vipType": "constant",
              "vipValue": "ipsec",
              "vipObjectType": "object"
            },
            "priority-order": [
              "encap",
              "preference",
              "weight"
            ]
          }
        ],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "encap"
        ]
      },
      "group": {
        "vipObjectType": "list",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_group"
      },
      "border": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_border"
      },
      "color": {
        "value": {
          "vipObjectType": "object",
          "vipType": "constant",
          "vipValue": "mpls",
          "vipVariableName": "vpn_if_tunnel_color_value"
        },
        "restrict": {
          "vipObjectType": "node-only",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_color_restrict"
        }
      },
      "carrier": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "default",
        "vipVariableName": "vpn_if_tunnel_carrier"
      },
      "bind": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_bind"
      },
      "allow-service": {
        "dhcp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_dhcp"
        },
        "dns": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_dns"
        },
        "icmp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_icmp"
        },
        "sshd": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_sshd"
        },
        "ntp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_ntp"
        },
        "stun": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_stun"
        },
        "all": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_all"
        },
        "bgp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_bgp"
        },
        "ospf": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_ospf"
        },
        "netconf": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_netconf"
        },
        "snmp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_snmp"
        },
        "https": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_https"
        }
      },
      "max-control-connections": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_max_control_connections"
      },
      "vbond-as-stun-server": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_vbond_as_stun_server"
      },
      "exclude-controller-group-list": {
        "vipObjectType": "list",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_exclude_controller_group_list"
      },
      "vmanage-connection-preference": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 5,
        "vipVariableName": "vpn_if_tunnel_vmanage_connection_preference"
      },
      "port-hop": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "true",
        "vipVariableName": "vpn_if_tunnel_port_hop"
      },
      "low-bandwidth-link": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_low_bandwidth_link"
      },
      "last-resort-circuit": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_last_resort_circuit"
      },
      "nat-refresh-interval": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 5,
        "vipVariableName": "vpn_if_tunnel_nat_refresh_interval"
      },
      "hello-interval": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 1000,
        "vipVariableName": "vpn_if_tunnel_hello_interval"
      },
      "hello-tolerance": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 12,
        "vipVariableName": "vpn_if_tunnel_hello_tolerance"
      },
      "tloc-extension-gre-to": {
        "dst-ip": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipVariableName": "vpn_if_tunnel_tloc_ext_gre_to_dst_ip"
        }
      },
      "control-connections": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "true",
        "vipVariableName": "control_connections"
      }
    },
    "ip-directed-broadcast": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "false",
      "vipVariableName": "vpn_if_ip-directed-broadcast"
    },
    "ipv6": {
      "access-list": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "direction"
        ]
      },
      "address": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "",
        "vipVariableName": "vpn_if_ipv6_ipv6_address"
      },
      "dhcp-helper-v6": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "arp": {
      "ip": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "addr"
        ]
      }
    },
    "vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    },
    "ipv6-vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    }
  },
  "gTemplateClass": "cedge",
  "templateDefinition": {
    "if-name": {
      "vipObjectType": "object",
      "vipType": "variableName",
      "vipValue": "",
      "vipVariableName": "WAN_MPLS_PHYS_INTF"
    },
    "description": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_description"
    },
    "ip": {
      "address": {
        "vipObjectType": "object",
        "vipType": "variableName",
        "vipValue": "",
        "vipVariableName": "WAN_MPLS_IP_ADDR"
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "dhcp-helper": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_dhcp_helper"
    },
    "flow-control": {},
    "clear-dont-fragment": {},
    "pmtu": {},
    "mtu": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1500,
      "vipVariableName": "vpn_if_ip_mtu"
    },
    "static-ingress-qos": {},
    "tcp-mss-adjust": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tcp_mss_adjust"
    },
    "mac-address": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_mac_address"
    },
    "speed": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_speed"
    },
    "duplex": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_duplex"
    },
    "shutdown": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "false",
      "vipVariableName": "vpn_if_shutdown"
    },
    "arp-timeout": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1200,
      "vipVariableName": "vpn_if_arp_timeout"
    },
    "autonegotiate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "true",
      "vipVariableName": "vpn_if_autonegotiate"
    },
    "shaping-rate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "rewrite_shaping_rate"
    },
    "qos-map": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "qos_map"
    },
    "tracker": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tracker"
    },
    "bandwidth-upstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_upstream"
    },
    "bandwidth-downstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_downstream"
    },
    "block-non-source-ip": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "false",
      "vipVariableName": "vpn_if_block_non_source_ip"
    },
    "rewrite-rule": {
      "rule-name": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "rewrite_rule_name"
      }
    },
    "tloc-extension": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tloc_extension"
    },
    "load-interval": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 30,
      "vipVariableName": "vpn_if_load_interval"
    },
    "icmp-redirect-disable": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "true",
      "vipVariableName": "vpn_if_icmp_redirect_disable"
    },
    "tloc-extension-gre-from": {
      "src-ip": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_src_ip"
      },
      "xconnect": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_xconnect"
      }
    },
    "access-list": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "direction"
      ]
    },
    "tunnel-interface": {
      "encapsulation": {
        "vipType": "constant",
        "vipValue": [
          {
            "preference": {
              "vipObjectType": "object",
              "vipType": "ignore",
              "vipVariableName": "vpn_if_tunnel_ipsec_preference"
            },
            "weight": {
              "vipObjectType": "object",
              "vipType": "ignore",
              "vipValue": 1,
              "vipVariableName": "vpn_if_tunnel_ipsec_weight"
            },
            "encap": {
              "vipType": "constant",
              "vipValue": "ipsec",
              "vipObjectType": "object"
            },
            "priority-order": [
              "encap",
              "preference",
              "weight"
            ]
          }
        ],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "encap"
        ]
      },
      "group": {
        "vipObjectType": "list",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_group"
      },
      "border": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_border"
      },
      "color": {
        "value": {
          "vipObjectType": "object",
          "vipType": "constant",
          "vipValue": "mpls",
          "vipVariableName": "vpn_if_tunnel_color_value"
        },
        "restrict": {
          "vipObjectType": "node-only",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_color_restrict"
        }
      },
      "carrier": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "default",
        "vipVariableName": "vpn_if_tunnel_carrier"
      },
      "bind": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_bind"
      },
      "allow-service": {
        "dhcp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_dhcp"
        },
        "dns": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_dns"
        },
        "icmp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_icmp"
        },
        "sshd": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_sshd"
        },
        "ntp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_ntp"
        },
        "stun": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_stun"
        },
        "all": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_all"
        },
        "bgp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_bgp"
        },
        "ospf": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_ospf"
        },
        "netconf": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_netconf"
        },
        "snmp": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "false",
          "vipVariableName": "vpn_if_tunnel_snmp"
        },
        "https": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipValue": "true",
          "vipVariableName": "vpn_if_tunnel_https"
        }
      },
      "max-control-connections": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_max_control_connections"
      },
      "vbond-as-stun-server": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_vbond_as_stun_server"
      },
      "exclude-controller-group-list": {
        "vipObjectType": "list",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tunnel_exclude_controller_group_list"
      },
      "vmanage-connection-preference": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 5,
        "vipVariableName": "vpn_if_tunnel_vmanage_connection_preference"
      },
      "port-hop": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "true",
        "vipVariableName": "vpn_if_tunnel_port_hop"
      },
      "low-bandwidth-link": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_low_bandwidth_link"
      },
      "last-resort-circuit": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "false",
        "vipVariableName": "vpn_if_tunnel_last_resort_circuit"
      },
      "nat-refresh-interval": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 5,
        "vipVariableName": "vpn_if_tunnel_nat_refresh_interval"
      },
      "hello-interval": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 1000,
        "vipVariableName": "vpn_if_tunnel_hello_interval"
      },
      "hello-tolerance": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": 12,
        "vipVariableName": "vpn_if_tunnel_hello_tolerance"
      },
      "tloc-extension-gre-to": {
        "dst-ip": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipVariableName": "vpn_if_tunnel_tloc_ext_gre_to_dst_ip"
        }
      },
      "control-connections": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "true",
        "vipVariableName": "control_connections"
      }
    },
    "ip-directed-broadcast": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "false",
      "vipVariableName": "vpn_if_ip-directed-broadcast"
    },
    "ipv6": {
      "access-list": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "direction"
        ]
      },
      "address": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "",
        "vipVariableName": "vpn_if_ipv6_ipv6_address"
      },
      "dhcp-helper-v6": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "arp": {
      "ip": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "addr"
        ]
      }
    },
    "vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    },
    "ipv6-vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    }
  },
  "attachedMastersCount": 0,
  "configType": "xml",
  "createdOn": 1624480017622,
  "@rid": 442,
  "factoryDefault": "false",
  "feature": "vmanage-default",
  "templateName": "TEST-WAN-MPLS",
  "createdBy": "admin",
  "templateDescription": "TEST-WAN-MPLS-DESCRIPTION"
}
testjson = json.dumps(testdict)
class vManageAPI:
    def __init__(self, vmanage_url, jsessionid, token, get_header, post_header):
        self.url = vmanage_url
        self.jsessionid = jsessionid
        self.token = token
        self.get_header = get_header
        self.post_header = post_header
        self.base_api_url = self.url + '/dataservice/'

    def get_api(self, api_endpoint_url):
        api_call_url = self.base_api_url + api_endpoint_url
        get_api_call = requests.get(url=api_call_url, headers=self.get_header, verify=False)
        get_api_call.raise_for_status()
        response = get_api_call.json()
        response_data = response['data']
        return response_data

    def post_api(self, api_endpoint_url):
        api_call_url = self.base_api_url + api_endpoint_url
        post_api_call = requests.post(url=api_call_url, headers=self.post_header, data=testjson, verify=False)
        print(post_api_call.content)