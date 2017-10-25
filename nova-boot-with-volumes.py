import argparse
import os
# from novaclient import client as novacl
import subprocess

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client

parser = argparse.ArgumentParser()
parser.add_argument(
    'amount', metavar='N', type=int,
    help='Amount of nova instances to boot')
args = parser.parse_args()

auth = v3.Password(auth_url='http://127.0.0.1:5000/v3',
                   username=os.environ['OS_USERNAME'],
                   password=os.environ['OS_PASSWORD'],
                   project_name=os.environ['OS_PROJECT_NAME'],
                   user_domain_id='default',
                   project_domain_id='default')
sess = session.Session(auth=auth)
nova = client.Client("2.1", session=sess)

# nova = novacl.Client(
#     '2', os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
#     os.environ['OS_TENANT_NAME'], os.environ['OS_TENANT_NAME'],
#     os.environ['OS_AUTH_URL'], connection_pool=True)
fl = nova.flavors.find(name='m1.nano')
im = nova.images.find(name='cirros-0.3.4-x86_64-uec')
for i in range(args.amount):
    subprocess.call([
        'nova', 'boot', '--flavor', fl.id, '--block-device',
        'source=image,id=%s,dest=volume,size=1,shutdown=remove,bootindex=0' % (
            im.id), 'vol-%s' % i])
