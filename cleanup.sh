for list in `zfs list -t snapshot | grep "pool1/iscsi/" | awk '{print $1}'` ; do zfs destroy $list; done
for list in `zfs list | grep "pool1/iscsi/" | awk '{print $1}'` ; do zfs destroy $list; done
for list in `zfs list -t snapshot | grep "pool1/nfs_share/share" | awk '{print $1}'` ; do zfs destroy $list; done
for list in `zfs list | grep "pool1/nfs_share/share-" | awk '{print $1}'` ; do zfs destroy $list; done
for list in `zfs list -t snapshot | grep "pool1/nfs_share/volume-" | awk '{print $1}'` ; do zfs destroy $list; done
for list in `zfs list | grep "pool1/nfs_share/volume-" | awk '{print $1}'` ; do zfs destroy $list; done 
sudo svcadm restart nms

for list in `neadm iscsi list iscsi | grep "volume-" | awk '{print $7}'` ; do neadm iscsi delete iscsi $list; done 


for i in $(filesystem list -r -O basic -o path | grep QA/nfs_share/);do filesystem destroy -fyr $i;done


ns5:
for i in $(fs list -O basic -o path | grep volume-); do fs destroy -fyRr $i; done
for i in $(vol list -O basic -o path | grep volume-); do vol destroy -yRr $i; done