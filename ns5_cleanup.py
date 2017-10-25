import subprocess

snap_list = subprocess.Popen('zfs list -t snapshot', shell=True,
                             stdout=subprocess.PIPE)
output, unused_err = snap_list.communicate()
out_list = output.split('\n')

for i in out_list:
    if i.startswith('/QA/nfs_share/vol') or i.startswith('QA/iscsi/vol'):
        try:
            subprocess.check_call(['zfs', 'destroy', '-R', i.split()[0]])
        except subprocess.CalledProcessError as e:
            print e.message


zfs_list = subprocess.Popen('zfs list', shell=True, stdout=subprocess.PIPE)
output, unused_err = zfs_list.communicate()
out_list = output.split('\n')

for i in out_list:
    if i.startswith('/QA/nfs_share/vol') or i.startswith('QA/iscsi/vol'):
        try:
            subprocess.check_call(['zfs', 'destroy', '-R', i.split()[0]])
        except subprocess.CalledProcessError as e:
            print e.message
