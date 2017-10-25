import subprocess

folder = 'cindervolumes'

zfs_list = subprocess.Popen(['zfs', 'list', '-t', 'volume'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = zfs_list.communicate()
vol_dict = {}
for l in out.split('\n'):
    print l
    if '/volume-' in l:
        vol_dict[l.split()[0]] = None

lu_list = subprocess.Popen(['stmfadm', 'list-lu', '-v'],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = lu_list.communicate()
for l in out.split('LU Name: '):
    for row in l.split('\n'):
        if row.strip().startswith('Data File'):
            data_file = row.split(':')[1].strip()
            for vol in vol_dict:
                if vol in data_file:
                    zvol = data_file.split('/')[-1]
                    new_file = '%s%s/%s' % (
                        data_file.strip(zvol), folder, zvol)
                    vol_dict[vol] = {'data_file': new_file}
                    lu_name = l.split('\n')[0]
                    vol_dict[vol]['lu_name'] = lu_name
                    lu_list = subprocess.Popen(
                        ['stmfadm', 'list-view', '-l', lu_name],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    view, err = lu_list.communicate()
                    for line in view.split('\n'):
                        if 'LUN' in line:
                            vol_dict[vol]['lun'] = line.split(': ')[1]
                        if 'Target group' in line:
                            vol_dict[vol]['tg'] = line.split(': ')[1]

for vol in vol_dict:
    parts = vol.split('/')
    new_vol = '%s/%s/%s' % (parts[0], folder, parts[1])
    subprocess.call(['zfs', 'rename', vol, new_vol])
    if vol_dict[vol]:
        subprocess.call(['stmfadm', 'delete-lu', vol_dict[vol]['lu_name']])
