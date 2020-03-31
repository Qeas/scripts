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

modprobe macvlan
docker network create -d macvlan --subnet 192.168.1.0/24 --gateway 192.168.1.1 -o parent=ens4f1 client-net
exit
neadm service configure nfs01 X-Container-Network-36BAFD395A0D5475F492F619BC72150F "client-net --ip 192.168.1.242"
neadm service enable nfs01
вот так
это вот на ноде делается
ssh  10.3.32.252
modprobe macvlan
docker network create -d macvlan --subnet 192.168.1.0/24 --gateway
192.168.1.1 -o parent=ens4f1 client-net
