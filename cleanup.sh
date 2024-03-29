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
for i in $(fs list -O basic -o path | grep csiDriverDataset/sanity); do fs destroy -fyRr $i; done
for i in $(fs list -O basic -o path | grep csiDriverDataset/sanity); do fs destroy -fyRr $i; done
for i in $(snap list -O basic -o path | grep nginx-persistent@snapshot-); do snap destroy -yRr $i; done

for i in $(lunmapping list -O basic -o id ); do lunmapping destroy -u $i; done
for i in $(iscsitarget list -O basic -o name | grep "-"); do iscsitarget destroy $i; done
for i in $(targetgroup list -O basic -o name | grep "-"); do targetgroup destroy $i; done
