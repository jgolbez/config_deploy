# Import Section
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class Authentication:
    def __init__(self, vmanage_url, vmanage_login_cred):
        self.url = vmanage_url
        self.cred = vmanage_login_cred
        # Static URL variables for construcing API calls
        self.login_url = self.url + '/j_security_check'
        self.token_url = self.url + '/dataservice/client/token'

    def login(self):
        vmanage_login_session = requests.session()
        login_result = vmanage_login_session.post(url=self.login_url, data=self.cred, verify=False)
        login_result.raise_for_status()
        # Add error handling for failed login based on returned data as status_code always returns 200
        # x-frame-options: DENY is in failed login header dict, maybe match on that
        #DEBUG print(login_result.headers)
        login_result_text = login_result.headers['set-cookie']
        split_headers = login_result_text.split(';')
        self.jsessionid = split_headers[0]
        return self.jsessionid
    def get_token(self):
        token_header = {'Cookie': self.jsessionid}
        token_response = requests.get(url=self.token_url, headers=token_header, verify=False)
        if token_response.status_code == 200:
            self.token = token_response.text
            return self.token
        else:
            return None

