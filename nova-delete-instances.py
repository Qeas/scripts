import os
# from novaclient import client as novacl
import subprocess
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client


auth = v3.Password(auth_url='http://127.0.0.1:5000/v3',
                   username=os.environ['OS_USERNAME'],
                   password=os.environ['OS_PASSWORD'],
                   project_name=os.environ['OS_PROJECT_NAME'],
                   user_domain_id='default',
                   project_domain_id='default')
sess = session.Session(auth=auth)
nova = client.Client("2.1", session=sess)
servers = nova.servers.list()
for s in servers:
    subprocess.call([
        'nova', 'delete', s.id])
# nova.flavors.list()
# nova = novacl.Client(
#     '2', os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
#     os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL'])
