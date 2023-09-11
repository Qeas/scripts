
echo '
[[local|localrc]]
disable_service etcd3
enable_service tempest
enable_plugin red git@github.com:DDNStorage/red-cinder-driver.git

GIT_BASE="https://opendev.org"
OVN_L3_CREATE_PUBLIC_NETWORK="True"
NEUTRON_CREATE_INITIAL_NETWORKS="True"
FLOATING_RANGE="172.24.5.0/24"
PUBLIC_NETWORK_GATEWAY="172.24.5.1"
NETWORK_GATEWAY="10.1.0.1"
FIXED_RANGE="10.1.0.0/20"
IPV4_ADDRS_SAFE_TO_USE="10.1.0.0/20"
NOVNC_FROM_PACKAGE="False"
FORCE="yes"
DATABASE_USER="root"
SERVICE_LOCAL_HOST="127.0.0.1"
ADMIN_PASSWORD="stack"
DATABASE_PASSWORD="stack"
RABBIT_PASSWORD="stack"
SERVICE_PASSWORD="stack"
SERVICE_TOKEN="stack"
DEST="/opt/stack"
CIDIR="/opt/stack/ci"
LOGDIR="/opt/stack/logs"
SCREEN_LOGDIR="/opt/stack/logs"
LOGFILE="/opt/stack/logs/stack.log"
VIRT_DRIVER="libvirt"
GIT_DEPTH="1"
ROOTSLEEP="0"
API_WORKERS="2"
BUILD_TIMEOUT="600"
SERVICE_TIMEOUT="600"
IP_VERSION="4"
# CIRROS_VERSION="0.3.6"
API_RATE_LIMIT="False"
INSTALL_TEMPEST="True"
TEMPEST_RUN_VALIDATION="True"
# DEFAULT_INSTANCE_USER="cirros"
# DEFAULT_INSTANCE_PASSWORD="cubswin:)"
CINDER_ISCSI_HELPER="tgtadm"
CINDER_IMG_CACHE_ENABLED="False"
CINDER_COORDINATION_URL="file://\$state_path"
SYSLOG="False"
USE_SCREEN="False"
USE_SYSTEMD="True"
USE_JOURNAL="True"
ENABLE_VOLUME_MULTIATTACH="False"
TEMPEST_VOLUME_MANAGE_VOLUME="False"
TEMPEST_VOLUME_MANAGE_SNAPSHOT="False"
TEMPEST_VOLUME_SNAPSHOT="False"
TEMPEST_VOLUME_CLONE="False"
TEMPEST_VOLUME_BACKEND_NAMES=red
LOG_COLOR=True
KEYSTONE_SERVICE_URI=127.0.0.1
TEMPEST_VOLUME_DRIVER=cinder.volume.drivers.red.nvmeof.RedNvmeOFDriver
TEMPEST_VOLUME_VENDOR="Red"
TEMPEST_STORAGE_PROTOCOL=NVMeOF
TEMPEST_HTTP_IMAGE=http://127.0.0.1/
TEMPEST_LOG_DIR=/opt/stack/tempest
TEMPEST_LOG_FILE=tempest.log
TEMPEST_VOLUME_REVERT_TO_SNAPSHOT=false

CINDER_ENABLED_BACKENDS=red
[[post-config|$CINDER_CONF]]
[DEFAULT]
suppress_requests_ssl_warning = True
verify_glance_signatures = disabled
executor_thread_pool_size = 1

[red]
volume_driver=cinder.volume.drivers.red.nvmeof.RedNvmeOFDriver
red_rest_address=ak-redvm-3.virts.devintel.redlab.datadirectnet.com
red_user=realm_admin
red_password=abcdabcd
red_cluster=red
red_tenant=red
red_subtenant=red
red_dataset=red
volume_backend_name=red
red_data_address=172.25.51.190
image_volume_cache_enabled = false

[[post-config|$NOVA_CONF]]
[libvirt]
cpu_mode = custom
' > local.conf

./stack.sh
