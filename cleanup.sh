for list in `zfs list | grep "pool1/nfs_share/volume-" | awk '{print $1}' ` ; do zfs destroy $list ; done
