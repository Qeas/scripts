import json
import requests
url = 'https://10.3.196.34:443/'
username = 'admin'
password = 'lustre'
requests.packages.urllib3.disable_warnings()
session = requests.session()
session.headers = {"Accept": "application/json", "Content-type": "application/json"}
session.verify = False
response = session.get(url + "api/host/")
if not 200 <= response.status_code < 300:
        raise RuntimeError("Failed to get host list")
data = json.loads(response.text)
# for host in data['objects']:
#     print(host)

response = session.post(url + "api/filesystem/", json.dumps({
  "osts": [{"volume_id": 22}],
  "mdt": {"id": 23},
  "mgt": {"volume_id": 24}
}))
# data = json.loads(response.text)
# count = len(data['objects'])
# print('Total volumes: %s' % count)
# for fs in data['objects']:
#     print('%s: %s' % (fs['name'], fs['mount_path']))
print(response)


# response = session.get(url + "api/filesystem/")
# data = json.loads(response.text)
# count = len(data['objects'])
# print('Total fs: %s' % count)
# for fs in data['objects']:
#     print('%s: %s' % (fs['name'], fs['mount_path']))
# print(data)

# response = session.get(url + "api/volume/")
# data = json.loads(response.text)
# count = len(data['objects'])
# print('Total volumes: %s' % count)
# for fs in data['objects']:
#     print('%s: %s' % (fs['name'], fs['mount_path']))
# print(data)
