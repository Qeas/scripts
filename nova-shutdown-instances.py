from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client

auth = v3.Password(auth_url='http://127.0.0.1:5000/v3',
                   username='admin',
                   password='nexenta',
                   project_name='admin',
                   user_domain_id='default',
                   project_domain_id='default')
sess = session.Session(auth=auth)
nova = client.Client("2.1", session=sess)

vms = im = nova.servers.list()
for vm in vms:
    if vm.status == 'ACTIVE':
        nova.servers.stop(vm)
