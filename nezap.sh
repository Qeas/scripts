echo 'y' | /opt/nedge/sbin/nezap
for disk in b c d e k i l f g h 
do 
  dd if=/dev/zero of=/dev/sd$disk bs=2G count=1
  umount /dev/sd$disk 2>/dev/null || true
  hdparm -z /dev/sd$disk
done
rm -rf /root/nedge-chef-solo/*
rm -rf /opt/*
dpkg -P nedge-core

wget http://10.3.30.163/nedge-dev/nedeploy/2587/nedeploy-linux_2.0.0-2587_x64.tar.gz
wget http://10.3.30.163/nedge-dev/neadm/2587/neadm-linux_2.0.0-2587_x64.tar.gz
tar -xzf nedeploy-linux_2.0.0-2587_x64.tar.gz
tar -xzf neadm-linux_2.0.0-2587_x64.tar.gz

APT_REPO=http://10.3.30.163/nedge-dev/ubuntu16/2587

tmpl-newton-cinder-67

/etc/apt/apt.conf.d/10periodic

cinder --os-auth-url=http://127.0.0.1:5000/v2.0/ --os-username=admin --os-password=nexenta --os-tenant-name=admin --os-project-name=admin type-create test
