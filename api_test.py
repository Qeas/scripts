import api
import subprocess
import time


class Conf(dict):
	"""dot.notation access to dictionary attributes"""
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


dict_conf = {
	'red_rest_address': ['ak-redvm-3.virts.devintel.redlab.datadirectnet.com'],
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

backend_name = 'red-1'
cluster = 'red'
tenant = 'red'
subtenant = 'red'
dataset = 'red'
proto = api.NVMEOF

red_proxy = api.RedProxy(proto, cluster, tenant, subtenant, dataset, backend_name, conf)

def create_volume(name):
	payload = {}
	payload['name'] = name
	payload['block_size'] = 4096
	payload['nblocks'] = 268435456
	red_proxy.bdevs.create(payload)

def get_volume(name):
	return red_proxy.bdevs.get(name, None)

def expose_volume(name):
	return red_proxy.bdevs.expose(name, {"nvmfs":None})

def delete_volume(name):
	red_proxy.bdevs.delete(name, {})

def parse_bdev_info(bdev_info, multipath=False):
	xattrs = bdev_info.get('xattrs')
	if not xattrs:
		raise api.RedException(
			code='ENOENT', message='no xattrs in bdev_info')
	nvmeof = xattrs.get('RED_INTERNAL_NVMEOF')
	if not nvmeof:
		raise api.RedException(
			code='ENOENT', message='no RED_INTERNAL_NVMEOF in xattrs')
	return nvmeof[0]

def connect_volume(export):
	info = parse_bdev_info(export)
	# subprocess.call(['sudo', 'nvme', 'connect', '-t', 'tcp', '-a', info['ipaddress'], '-s', '4420', '-n', 'nqn.asddsa'])
	subprocess.call(['sudo', 'nvme', 'connect', '-t', 'tcp', '-a', info['ipaddress'], '-s', '4420', '-n', info['nqn']])

def disconnect_volume(export):
	info = parse_bdev_info(export)
	subprocess.call(['sudo', 'nvme', 'disconnect', '-n', info['nqn']])

def disconnect_all_volumes():
	subprocess.call(['sudo', 'nvme', 'disconnect-all'])

def nvme_list():
	subprocess.call(['sudo', 'nvme', 'list'])


create_volume('test-vol1')
exp1 = expose_volume('test-vol1')
connect_volume(exp1)
get_volume('test-vol1')
disconnect_volume(exp1)

delete_volume('test-vol1')




# if __name__ == '__main__':
def main():
	volume_amount = 5
	loops = 15
	def connect_loop():
		for i in range(volume_amount):
			name = 'test-vol%s' % i
			create_volume(name)
			export = expose_volume(name)
			connect_volume(export)
	def delete_loop():
		for i in range(volume_amount):
			name = 'test-vol%s' % i
			delete_volume(name)
	try:
		for i in range(loops):
			connect_loop()
			nvme_list()
			disconnect_all_volumes()
			delete_loop()
	except Exception as exc:
		print(exc)
		disconnect_all_volumes()
		for i in range(volume_amount):
			try:
				name = 'test-vol%s' % i
				delete_volume(name)
			except:
				pass

main()


# red_proxy.bdevs.list()
# payload = {
# 	'name': 'dev4',
# 	'block_size': 1024,
# 	'nblocks': 1073741824,
# 	'nvmf': {
# 		# 'instanceid': 1,
# 		'transport': 'TCP',
# 		'addrfam': 'IPv4',
# 	}
# }

# red_proxy.bdevs.create(payload)

# red_proxy.bdevs.get('dev4')
# red_proxy.bdevs.delete('dev4')
# red_proxy.bdevs.expose('dev4')
