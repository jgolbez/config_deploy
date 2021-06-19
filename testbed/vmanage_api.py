# Import Section

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Testing variables hard coded

"""
Ultimately replace hardcoded environment variables with user-defined via Web input. For now, test parameters 
are fine
"""
vmanage_ip = '192.168.0.175'
vmanage_url = f'https://{vmanage_ip}:8443'
vmanage_user = 'admin'
vmanage_pw = 'admin'
vmanage_login_cred = {'j_username': vmanage_user,
                      'j_password': vmanage_pw}


class vManage:
    def __init__(self, vmanage_ip, vmanage_url, vmanage_login_cred, vmanage_user="admin", vmanage_pw="admin"):
        self.ip = vmanage_ip
        self.url = vmanage_url
        self.user = vmanage_user
        self.pw = vmanage_pw
        self.cred = vmanage_login_cred
        # Static URL variables for construcing API calls
        self.login_url = self.url + '/j_security_check'

    def login(self):
        vmanage_login_session = requests.session()
        login_result = vmanage_login_session.post(url=vmanage_login_url, data=vmanage_login_cred, verify=False)
        print(login_result.status_code)
        print(login_result.headers)
