import os
from novaclient import client as novacl
import subprocess
# from cinderclient import client as cindercl


nova = novacl.Client(
    '2', os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
    os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL'])
servers = nova.servers.list()
for s in servers:
    subprocess.call([
        'nova', 'delete', s.id])
