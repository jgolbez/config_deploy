# Import Section
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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



