# Usage: 
# ip=$(ip a | grep 172.25. | awk '{print $2}' | awk -F / '{print $1}')
# python https_client.py --url https://$ip:443 --endpoint clusters/red/tenants/red/subtenants/red/datasets/red/bdevs --method GET --user storage_admin_001 --password abcdabcd
# python https_client.py --url https://$ip:443 --endpoint clusters/red/tenants/red/subtenants/red/datasets/red/bdevs --method POST --user storage_admin_001 --password abcdabcd --data '{"name": "rest-api-3", "block_size": 4096, "nblocks": 262144}'
# python https_client.py --url https://$ip:443 --endpoint clusters/red/tenants/red/subtenants/red/datasets/red/bdevs/rest-api-3/expose --method PUT --user storage_admin_001 --password abcdabcd --data '{"transport": "tcp", "addrfam": "ipv4", "ipaddrs": ["172.25.51.113"], "port": 4420}'
# python https_client.py --url https://$ip:443 --endpoint clusters/red/tenants/red/subtenants/red/datasets/red/bdevs/rest-api-3/unexpose --method POST --user storage_admin_001 --password abcdabcd --data '{"instanceId": null, "subsystemName": ""}'
python https_client.py --url https://ak-redvm-2.virts.devintel.redlab.datadirectnet.com:443 --endpoint clusters/red/tenants/red/subtenants/red/datasets --method GET --user realm_admin --password abcdabcd

import argparse
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HTTPSClient:
    def __init__(self, url, user, password):
        self.base_url = urljoin(url, "redapi/v1/")
        self.token = None
        self.user = user
        self.password = password
        self._update_token()
        self.session = requests.Session()

    def _get(self, endpoint, **kwargs):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.get(url, verify=False, **kwargs)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise http_err
        except Exception as err:
            print(f'Other error occurred: {err}')
            raise err

    def _post(self, endpoint, data=None, **kwargs):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.post(url, verify=False, data=data, **kwargs)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise http_err
        except Exception as err:
            print(f'Other error occurred: {err}')
            raise err

    def _put(self, endpoint, data=None, **kwargs):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.put(url, verify=False, data=data, **kwargs)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise http_err
        except Exception as err:
            print(f'Other error occurred: {err}')
            raise err

    def _delete(self, endpoint, **kwargs):
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.delete(url, verify=False, **kwargs)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise http_err
        except Exception as err:
            print(f'Other error occurred: {err}')
            raise err

    def _update_token(self):
        auth_url = urljoin(self.base_url, 'auth_user')
        headers = {
            'user_id': self.user,
            'password': self.password
        }
        response = requests.get(auth_url, headers=headers, verify=False)
        response.raise_for_status()
        self.token = response.json()['data']['token']

    def headers(self):
        return {'Token': self.token}

    def call(self, method, endpoint, data=None):
        if method not in ['GET', 'POST', 'PUT', 'DELETE']:
            raise ValueError(f'Invalid method {method}')

        url = urljoin(self.base_url, endpoint)
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        if method == 'GET':
            return self._get(url, headers=headers)
        elif method == 'POST':
            return self._post(url, data=data, headers=headers)
        elif method == 'PUT':
            return self._put(url, data=data, headers=headers)
        elif method == 'DELETE':
            return self._delete(url, headers=headers)

def main():
    parser = argparse.ArgumentParser(description='HTTP/HTTPS client')
    parser.add_argument('--url', type=str, help='Base URL of the API', required=True)
    parser.add_argument('--endpoint', type=str, help='API endpoint', required=True)
    parser.add_argument('--method', type=str, help='HTTP method', required=False)
    parser.add_argument('--data', type=str, help='data for POST calls', required=False)
    parser.add_argument('--user', type=str, help='User ID for authentication', required=True)
    parser.add_argument('--password', type=str, help='Password for authentication', required=True)
    args = parser.parse_args()

    method = args.method.upper() or 'GET'
    http_client = HTTPSClient(args.url, args.user, args.password)
    response = http_client.call(args.method, args.endpoint, args.data)
    if response:
        print(response.text)

if __name__ == '__main__':
    main()
