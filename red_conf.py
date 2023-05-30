import api


class Conf(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


dict_conf = {
	'red_rest_address': ['ak-redvm-intel-2.virts.devintel.redlab.datadirectnet.com'],
	'red_rest_port': 443,
	'red_user': 'storage_admin_001',
	'red_password': 'abcdabcd',
	'red_use_https': True,
	'red_rest_retry_count': 1,
	'red_rest_backoff_factor': 1,
	'driver_ssl_cert_verify': False,
	'red_rest_connect_timeout': 1,
	'red_rest_read_timeout': 1,
	'red_rest_protocol': 'https',
}

conf = Conf(dict_conf)

backend_name = 'red'
cluster = 'red'
tenant = 'red'
subtenant = 'red'
dataset = 'red'
proto = api.NVMEOF

red_proxy = api.RedProxy(proto, cluster, tenant, subtenant, dataset, backend_name, conf)
red_proxy.bdevs.list()

payload = {
	'name': 'dev4',
	'block_size': 1024,
	'nblocks': 1073741824,
	'nvmf': {
		# 'instanceid': 1,
		'transport': 'TCP',
		'addrfam': 'IPv4',
	}
}

red_proxy.bdevs.create(payload)

red_proxy.bdevs.get('dev4')
red_proxy.bdevs.delete('dev4')
red_proxy.bdevs.expose('dev4')
