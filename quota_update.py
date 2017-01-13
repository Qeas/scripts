import subprocess


s = subprocess.check_output(['openstack', 'project', 'list'])
s = s.split(
    '|\n+----------------------------------+--------------------+\n|')[1]
val = '100000000'
for i in range(len(s.strip().split('|\n|'))):
    pr_id = s.strip().split('|\n|')[i].split('|')[0].strip()
    subprocess.call([
        'cinder', 'quota-update', '--gigabytes', val, '--volumes',
        val, '--snapshots', val, pr_id])
    subprocess.call([
        'nova', 'quota-update', '--instances', val, 'cores', val, pr_id])
