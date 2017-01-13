import argparse
import os
from novaclient import client as novacl
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument(
    'amount', metavar='N', type=int,
    help='Amount of nova instances to boot')
args = parser.parse_args()

nova = novacl.Client(
    '2', os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
    os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL'])
fl = nova.flavors.find(name='m1.nano')
im = nova.images.find(name='cirros-0.3.4-x86_64-uec')
for i in range(args.amount):
    subprocess.call([
        'nova', 'boot', '--flavor', fl.id, '--block-device',
        'source=image,id=%s,dest=volume,size=1,shutdown=remove,bootindex=0' % (
            im.id), 'vol-%s' % i])
