# Imports
import sys
from vmanage_auth import Authentication
from vmanage_api import vManageAPI
import json

# Testing variables hard coded
"""
Ultimately replace hardcoded environment variables with user-defined via Web input. For now, test parameters 
are fine

vmanage_ip = '192.168.0.175'
vmanage_url = f'https://{vmanage_ip}:8443'
vmanage_user = 'admin'
vmanage_pw = 'admin'
vmanage_login_cred = {'j_username': vmanage_user,
                      'j_password': vmanage_pw}
"""

# Basic vManage Inputs - Replace with Web inputs
# TODO Normalize or validate inputs - also with web input
vmanage_ip = input('What is the IP address or hostname of the vManage?\n')
vmanage_port = input('What is the port number of the vManage API [8443]?\n')
if vmanage_port == '':
    vmanage_port = '8443'
vmanage_url = f'https://{vmanage_ip}:{vmanage_port}'
vmanage_user = input('What is the username of the vManage admin account [admin]?\n')
if vmanage_user == '':
    vmanage_user = 'admin'
vmanage_pw = input('What is the password of the vManage admin account [admin]?\n')
if vmanage_pw == '':
    vmanage_pw = 'admin'
vmanage_login_cred = {'j_username': vmanage_user,
                      'j_password': vmanage_pw}

vmanage_login = Authentication(vmanage_url, vmanage_login_cred)

jsessionid = vmanage_login.login()
token = vmanage_login.get_token()
if token is not None:
    post_header = {'Content-Type': "application/json", 'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    print('There is no XSRF-TOKEN available, POST commands will not be allowed. Please check credentials and '
          'JSESSIONID and log back into the API.')
    sys.exit()
get_header = {'Content-Type': "application/json", 'Cookie': jsessionid}
print('MOVING TO API CALL AS REQUESTED')
testget = vManageAPI(vmanage_url, jsessionid, token, get_header, post_header)
# Test call - Get list of devices - endpoint api url is /device
feature_templates = testget.get_api("template/feature")
# TODO Clean up what is returned so only relevant data is used
print(type(feature_templates[0]))
#print(feature_templates)
#print(json.dumps(feature_templates, indent=4))

for template in feature_templates:
    print(template["templateName"])
    print(template['templateDescription'])
    print(template['templateType'])
    print(template['deviceType'])
    print(json.dumps(json.loads(template["templateDefinition"]), indent=4))
