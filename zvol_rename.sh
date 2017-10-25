for list in `zfs list -t snapshot | grep "pool1/iscsi/" | awk '{print $1}'` ; do zfs destroy $list; done
