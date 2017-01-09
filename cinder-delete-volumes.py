import os
import subprocess
from cinderclient import client as cindercl


cinder = cindercl.Client(
    '2', os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'],
    os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL'])
volumes = cinder.volumes.list()
for v in volumes:
    subprocess.call(['cinder', 'delete', v.id])
